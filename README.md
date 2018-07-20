# TaiwanInvoice

[資料來源](https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/)

## Requirement
- Python3.x
- PyQuery==1.4.0
- requests==2.19.1

# Info
specialPrize = 特別獎  
grandPrize = 特獎  
firstPrize = 頭獎  
twoPrize = 二獎  
threeAwards = 三獎  
fourPrizes = 四獎  
fivePrize = 五獎  
sixPrize = 六獎  
addSixPrize = 增開六獎  

# Result Preview
```
getinvoice = invoice('10605')
print(getinvoice.getprize())

{'addSixPrize': {'number': '904'},
 'firstPrize': {'desc': '同期統一發票收執聯8位數號碼與頭獎號碼相同者獎金20萬元',
                'number': ['70628612', '87596250', '97294175']},
 'fivePrize': {'desc': '同期統一發票收執聯末4 位數號碼與頭獎中獎號碼末4 位相同者各得獎金1千元'},
 'fourPrizes': {'desc': '同期統一發票收執聯末5 位數號碼與頭獎中獎號碼末5 位相同者各得獎金4千元'},
 'grandPrize': {'desc': '同期統一發票收執聯8位數號碼與特獎號碼相同者獎金200萬元', 'number': '83660478'},
 'sixPrize': {'desc': '同期統一發票收執聯末3 位數號碼與 頭獎中獎號碼末3 位相同者各得獎金2百元'},
 'specialPrize': {'desc': '同期統一發票收執聯8位數號碼與特別獎號碼相同者獎金1,000萬元',
                  'number': '99768846'},
 'threeAwards': {'desc': '同期統一發票收執聯末6 位數號碼與頭獎中獎號碼末6 位相同者各得獎金1萬元'},
 'twoPrize': {'desc': '同期統一發票收執聯末7 位數號碼與頭獎中獎號碼末7 位相同者各得獎金4萬元'}}

getinvoice = invoice('10602')
print(getinvoice.getprize())

{'status': 'error'}

```
