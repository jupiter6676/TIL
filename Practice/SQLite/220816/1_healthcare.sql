SELECT COUNT(*) FROM healthcare;
SELECT COUNT(*) FROM healthcare WHERE age<10;
SELECT COUNT(*) FROM healthcare WHERE gender=1;
SELECT COUNT(*) FROM healthcare WHERE smoking=3 AND is_drinking=1;
SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 AND va_right>=2.0;
SELECT DISTINCT sido FROM healthcare;