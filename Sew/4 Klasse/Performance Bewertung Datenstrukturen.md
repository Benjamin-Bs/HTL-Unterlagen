# Performance Bewertung Datenstrukturen

Performance der Datenstrukturen im schlechtesten Fall:

| Datenstruktur            | Zugriff   | Einfügen  | Löschen   | Suchen    |
| ------------------------ |:---------:|:---------:|:---------:|:---------:|
| Array (List)             | O (1)     | O (1)     | O (n)     | O (n)     |
| Sortiertes Array         | O (1)     | O (n)     | O (log n) | O (log n) |
| Linked List              | O (n)     | O (1)     | O (n)     | O (n)     |
| Baum                     | O (n)     | O (1)     | O (n)     | O (n)     |
| Balancierter Baum        | O (log n) | O (log n) | O (log n) | O (log n) |
| HashMap                  | => Suchen | O (log n) | O (log n) | O (log n) |
| HashMap ohne Kollisionen | => Suchen | O (1)     | O (1)     | O (1)     |

Die Performance der HashMap bei Verwendung von Listen im Kollisionsfall beträgt  O (n). In Java wird jedoch ab einer gewissen Anzahl von Elementen ein balancierter Baum verwendet, dadruch beträgt die Performance O (log n)


