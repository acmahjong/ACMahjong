# ACMahjong

| key         | object    |                                                         |                                     |                    |
| ----------- | --------- | ------------------------------------------------------- | ----------------------------------- | ------------------ |
| start_match | type      | 0/1                                                     |                                     |                    |
|             | seat      | 0/1/2/3                                                 |                                     |                    |
|             |           |                                                         |                                     |                    |
| start_game  | kyoku     | 0/1/…/7                                                 |                                     |                    |
|             | bon       | 0/1/2…                                                  |                                     |                    |
|             | oya       | 0/1/2/3                                                 |                                     |                    |
|             |           |                                                         |                                     |                    |
| distribute  | tiles     | [](0-135)                                               |                                     |                    |
|             |           |                                                         |                                     |                    |
| event       | player    | 0/1/2/3                                                 |                                     |                    |
|             | type      | CHI/PON/KAN                                             |                                     |                    |
|             | tile      |                                                         |                                     |                    |
|             | closed    | 0/1                                                     |                                     |                    |
|             |           |                                                         |                                     |                    |
| discard     | player    | 0/1/2/3                                                 | wait for BOOL then wait for “event” |                    |
|             | tile      |                                                         |                                     |                    |
|             | tsumogiri |                                                         |                                     |                    |
|             |           |                                                         |                                     |                    |
| get_tile    | tile      |                                                         | wait for BOOL then wait for tile    | 自摸？切牌？暗杠？ |
|             |           |                                                         |                                     |                    |
| riichi      | player    | 0/1/2/3                                                 | then followed by diacard            |                    |
|             |           |                                                         |                                     |                    |
| end_game    | result    | [player, from, tiles:[], wintile, yi:[], fu:[], dan:[]] |                                     |                    |
|             | score     | [+-???,+-???,+-???,+-???]                               |                                     |                    |
|             | after     | []                                                      |                                     |                    |