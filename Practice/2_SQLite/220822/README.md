### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT *
FROM playlist_track AS A
ORDER BY A.PlaylistId DESC
LIMIT 5;
```



### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT *
FROM tracks AS B
ORDER BY B.TrackId
LIMIT 5;
```



### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
SELECT
  playlist_track.PlaylistId,
  tracks.TrackId,
  tracks.Name
FROM playlist_track JOIN tracks
ON playlist_track.TrackId = tracks.TrackId
ORDER BY playlist_track.PlaylistId DESC
LIMIT 10;
```



### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 

| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT
  playlist_track.PlaylistId,
  tracks.TrackId,
  tracks.Name
FROM playlist_track JOIN tracks
ON playlist_track.TrackId = tracks.TrackId
WHERE playlist_track.PlaylistId = 10
ORDER BY tracks.Name DESC
LIMIT 5;
```



### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks JOIN artists
ON tracks.Composer = artists.Name;
```



### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks LEFT JOIN artists
ON tracks.Composer = artists.Name;
```



### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

```plain
INNER JOIN은 행의 값이 같은 것만 출력하고, LEFT JOIN은 같지 않은 것도 출력하기 때문이다.
```



### 8. invoice_items 테이블의 데이터를 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT
  InvoiceLineId,
  InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;
```



### 9. invoices 테이블의 데이터를 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT
  InvoiceId,
  CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
```



### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT
  invoice_items.InvoiceLineId,
  invoices.InvoiceId
FROM invoice_items JOIN invoices
ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
```



### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT
  invoices.InvoiceId,
  customers.CustomerId
FROM invoices JOIN customers
ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
```



### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT
  invoice_items.InvoiceLineId,
  invoice_items.InvoiceId,
  customers.CustomerId
FROM invoices
  JOIN invoice_items
  ON invoices.InvoiceId = invoice_items.InvoiceId
  JOIN customers
  ON invoices.CustomerId = customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;
```



### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.

| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT
  invoices.CustomerId,
  COUNT(*)
FROM invoices JOIN invoice_items
ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY invoices.CustomerId
ORDER BY invoices.CustomerId
LIMIT 5;
```

```
CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```



### 14. 각 고객이 주문한 물건을, invoiceId를 기준으로 그룹을 나누어 그 개수를 출력

| 자유

```sql
SELECT
  invoices.CustomerId,
  invoices.InvoiceId,
  COUNT(*)
FROM invoices JOIN invoice_items
ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY invoices.CustomerId, invoice_items.InvoiceId
ORDER BY invoices.CustomerId;
```

