Angepasstes Konzept der MongoDB-Datenbank
Sammlung: Prices
Dokumentstruktur: Ein Dokument für jeden Ticker, das sowohl die Kursdaten als auch zusätzliche Informationen enthält.
{
    "ticker": "EOAN.DE",
    "data": [
        {"price": 150.0, "timestamp": "2023-10-23T09:00:00Z"},
        {"price": 151.2, "timestamp": "2023-10-24T09:00:00Z"},
        ...
    ],
    "info": {
        "address": "Brüsseler Platz 1, Essen, 45131, Germany",
        "phone": "49 201 184 00",
        "website": "https://www.eon.com",
        "industry": "Utilities - Diversified",
        ...
    }
}