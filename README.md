# 📊 Analiza danych sprzedażowych (Python + Pandas + Matplotlib)

## 📌 Opis projektu

Ten projekt to kompletny pipeline analizy danych sprzedażowych stworzony w Pythonie. Obejmuje on wczytanie danych, ich czyszczenie, preprocessing, obliczanie kluczowych wskaźników biznesowych (KPI), agregacje oraz wizualizacje.

Celem projektu jest szybka analiza wyników sprzedaży oraz identyfikacja najważniejszych trendów w danych.

---

## ⚙️ Technologie

- Python 3
- Pandas – analiza i przetwarzanie danych
- Matplotlib – wizualizacja danych

---

## 🧹 Proces analizy danych

### 1. Wczytanie danych
- Import danych z pliku CSV
- Walidacja wymaganych kolumn
- Czyszczenie tekstu (usuwanie zbędnych spacji)

### 2. Przetwarzanie danych (preprocessing)
- Konwersja dat do formatu datetime
- Konwersja wartości numerycznych (Price, Quantity)
- Usuwanie błędnych i pustych danych
- Usuwanie duplikatów
- Tworzenie nowych kolumn:
  - Revenue (przychód)
  - Month
  - DayOfWeek
  - Year

### 3. Analiza KPI
Projekt oblicza kluczowe wskaźniki biznesowe:

- liczba zamówień
- całkowity przychód
- średnia wartość zamówienia
- liczba unikalnych produktów
- liczba miast

### 4. Agregacja danych
Dane są grupowane według:

- miast
- produktów
- menedżerów
- typu zakupu
- metody płatności

### 5. Wizualizacja danych
Projekt generuje wykresy:

- 📊 przychód według miasta
- 📊 przychód według produktu
- 📈 trend sprzedaży w czasie
- 🥧 udział procent
