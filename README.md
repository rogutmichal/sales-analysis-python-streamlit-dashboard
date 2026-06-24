#  Analiza danych sprzedażowych (Python + Pandas + Matplotlib)

##  Opis projektu

Ten projekt to kompletny pipeline analizy danych sprzedażowych stworzony w Pythonie. Obejmuje on wczytanie danych, ich czyszczenie, preprocessing, obliczanie kluczowych wskaźników biznesowych (KPI), agregacje oraz wizualizacje. W projekcie wykorzystano zbiór danych "Restaurant Sales Data" autorstwa Data Science Lovers: https://www.kaggle.com/datasets/rohitgrewal/restaurant-sales-data/data

Celem projektu jest szybka analiza wyników sprzedaży oraz identyfikacja najważniejszych trendów w danych.

---

##  Technologie

- Python 3
- Pandas – analiza i przetwarzanie danych
- Matplotlib – wizualizacja danych
- Streamlit – interaktywny dashboard webowy
- Plotly Express – interaktywne wykresy
---

##  Proces analizy danych

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

-  przychód według miasta

  <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/266549a0-6374-412a-a5d7-de9e87175ec2" />

-  przychód według produktu

<img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/93d2e350-0acc-498f-b5c0-b6793ff936c5" />

-  trend sprzedaży w czasie

<img width="1200" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/6775a9dd-5937-47c6-a307-205ff7845ce1" />

-  przychody według metody kupna

<img width="800" height="500" alt="Figure_4" src="https://github.com/user-attachments/assets/d5109b31-b79f-4a48-9efe-09bff8237a8f" />


-  przychody według metody płatności

<img width="700" height="700" alt="Figure_5" src="https://github.com/user-attachments/assets/2d28a723-12c0-438b-88f7-799f0e47741d" />



---

## Aktualizacja – Interaktywny Dashboard (Streamlit + Plotly)

Projekt został rozszerzony o interaktywny dashboard webowy umożliwiający analizę danych sprzedażowych w czasie rzeczywistym.

### Nowe technologie

* Streamlit – budowa aplikacji webowej
* Plotly Express – interaktywne wizualizacje danych

### Dodane funkcjonalności

#### Interaktywne filtry

Użytkownik może filtrować dane według:

* miasta
* produktu
* menedżera

Po zastosowaniu filtrów wszystkie wskaźniki oraz wykresy aktualizują się automatycznie.

#### Dashboard KPI

Dodano dynamiczne wskaźniki biznesowe:

* całkowity przychód
* liczba zamówień
* średnia wartość zamówienia
* liczba unikalnych produktów

#### Interaktywne wizualizacje

Dashboard prezentuje:

* trend przychodów w czasie
* przychód według miasta
* wyniki sprzedażowe menedżerów
* TOP 5 najlepiej sprzedających się produktów
* podział metod płatności
* podział typów zakupów

#### Optymalizacja wydajności

Zastosowano mechanizm `@st.cache_data`, który ogranicza ponowne wczytywanie oraz przetwarzanie danych, poprawiając wydajność aplikacji.

### Widok dashboardu
<img width="1891" height="440" alt="image" src="https://github.com/user-attachments/assets/79f42c1c-95de-4304-813c-080afc3a657a" />


<img width="1447" height="557" alt="image" src="https://github.com/user-attachments/assets/81a840a7-9dbe-4662-8fa8-9dfefff259a0" />


<img width="1447" height="625" alt="image" src="https://github.com/user-attachments/assets/6bbd011f-9cd8-4e37-9491-0ff4faf014db" />


<img width="1457" height="561" alt="image" src="https://github.com/user-attachments/assets/1d48422a-15a9-44e4-b45d-9885a7d8739f" />




