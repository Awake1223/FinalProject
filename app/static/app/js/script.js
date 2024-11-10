const data = {
    "disclaimer": "https://www.cbr-xml-daily.ru/#terms",
    "date": "2024-10-30",
    "rates": {
        "AUD": 0.01565077,
        "AZN": 0.0174670658,
        "GBP": 0.0079060758,
        "AMD": 3.97693378,
        "BYN": 0.034037,
        "BGN": 0.0185761,
        "BRL": 0.05855075,
        "HUF": 3.842444,
        "VND": 249.1826808,
        "HKD": 0.0796907997,
        "GEL": 0.0280038,
        "DKK": 0.070839,
        "AED": 0.03773399795,
        "USD": 0.010274736,
        "EUR": 0.00948429,
        "EGP": 0.500482966,
        "INR": 0.8638786,
        "IDR": 161.611199,
        "KZT": 5.012129,
        "CAD": 0.0142767,
        "QAR": 0.0374,
        "KGS": 0.88156989968,
        "CNY": 0.073554,
        "MDL": 0.184824,
        "NZD": 0.01719045998,
        "NOK": 0.11313816999,
        "PLN": 0.0413568,
        "RON": 0.04730078,
        "XDR": 0.007727169,
        "SGD": 0.013614,
        "TJS": 0.1095019,
        "THB": 0.346968,
        "TRY": 0.35159889598,
        "TMT": 0.0359615,
        "UZS": 131.4644349,
        "UAH": 0.424646,
        "CZK": 0.2397196,
        "SEK": 0.1089494,
        "CHF": 0.00889998,
        "RSD": 1.112214675,
        "ZAR": 0.1819359,
        "KRW": 14.2510638,
        "JPY": 1.571212866
    }
};

const tbody = document.querySelector('#exchangeRates tbody');

for (const [currency, rate] of Object.entries(data.rates)) {
    const row = document.createElement('tr');
    const cellCurrency = document.createElement('td');
    const cellRate = document.createElement('td');

    cellCurrency.textContent = currency;
    cellRate.textContent = rate;

    row.appendChild(cellCurrency);
    row.appendChild(cellRate);
    tbody.appendChild(row);
}