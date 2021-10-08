# marketstack_to_plot
plots the price symbol to terminal

To run it:
- get an apikey from https://api.marketstack.com
- create a new file config.py:
```angular2html
api_key = 'YOUR_ACCESS_KEY'
symbols = 'APPL'
```
- replace YOUR_ACCESS_KEY in the api_key variable from config.py with the correct apikey
- change the symbols variable (default APPL) 


```angular2html
  4000 +------------------------------------------------+
       |                                             *  |
  3500 |                                         * **** |
       |                                        ******* |
  3000 |                                        ****    |
       |                                        *       |
  2500 |                                       **       |
       |                                      ***       |
  2000 |                                *  ** **        |
       |                               *********        |
  1500 |                             *** **             |
       |                            ***  *              |
  1000 |                          ***                   |
       |                   ********                     |
   500 |           **   *******                         |
       |  ****************                              |
     0 +------------------------------------------------+
    1.3e+0 1.35e+ 1.4e+0 1.45e+ 1.5e+0 1.55e+ 1.6e+ 1.65e+09

```
