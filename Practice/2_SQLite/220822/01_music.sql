-- 1.
SELECT *
FROM playlist_track AS A
ORDER BY A.PlaylistId DESC
LIMIT 5;

-- 2.
SELECT *
FROM tracks AS B
ORDER BY B.TrackId
LIMIT 5;

-- 3.
SELECT
  playlist_track.PlaylistId,
  tracks.TrackId,
  tracks.Name
FROM playlist_track JOIN tracks
ON playlist_track.TrackId = tracks.TrackId
ORDER BY playlist_track.PlaylistId DESC
LIMIT 10;

-- 4.
SELECT
  playlist_track.PlaylistId,
  tracks.TrackId,
  tracks.Name
FROM playlist_track JOIN tracks
ON playlist_track.TrackId = tracks.TrackId
WHERE playlist_track.PlaylistId = 10
ORDER BY tracks.Name DESC
LIMIT 5;

-- 5.
SELECT COUNT(*)
FROM tracks JOIN artists
ON tracks.Composer = artists.Name;

-- 6.
SELECT COUNT(*)
FROM tracks LEFT JOIN artists
ON tracks.Composer = artists.Name;

-- 7.
-- INNER JOIN은 행의 값이 같은 것만 출력하고, 
-- LEFT JOIN은 같지 않은 것도 출력하기 때문이다.

-- 8.
SELECT
  InvoiceLineId,
  InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;

-- 9.
SELECT
  InvoiceId,
  CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;

-- 10.
SELECT
  invoice_items.InvoiceLineId,
  invoices.InvoiceId
FROM invoice_items JOIN invoices
ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;

-- 11.
SELECT
  invoices.InvoiceId,
  customers.CustomerId
FROM invoices JOIN customers
ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;

-- 12.
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

-- 13-1.
SELECT
  invoices.CustomerId,
  COUNT(*)
FROM invoices JOIN invoice_items
ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY invoices.CustomerId
ORDER BY invoices.CustomerId
LIMIT 5;

-- 13-2.
-- 각 고객(CustomerId)이 시킨 송장 번호(InvoiceId)
SELECT * FROM invoices A
INNER JOIN customers B
ON A.CustomerId = B.CustomerId;

SELECT
  C.CustomerId,
  COUNT(*)
FROM invoice_items AS A
INNER JOIN (
  SELECT * FROM invoices A
  INNER JOIN customers B
  ON A.CustomerId = B.CustomerId
  ) AS C
ON A.invoiceid = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId
LIMIT 5;

-- 14. 자유
SELECT * FROM invoices
WHERE CustomerId = 1;

SELECT *
FROM invoice_items JOIN invoices
ON invoice_items.InvoiceId = invoices.InvoiceId
WHERE invoices.CustomerId = 1;

SELECT
  invoices.CustomerId,
  invoices.InvoiceId,
  COUNT(*)
FROM invoices JOIN invoice_items
ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY invoices.CustomerId, invoice_items.InvoiceId
ORDER BY invoices.CustomerId;