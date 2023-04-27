select
shop.品牌名称
,shop.城市
,shop.门店名称
,sum(shop.GMV) GMV
,round(sum(cpc.cpc总费用),2) cpc总费用
from ddm.shop
left join ddm.cpc
on shop.门店ID = cpc.门店ID
and shop.日期 = cpc.日期
left join
(
   select
   门店ID
   ,下单日期
   ,sum(用户实付) 用户实付
   from ods.orders
    group by 1,2
) orders
on shop.门店ID = orders.门店ID
and shop.日期 = orders.下单日期
group by 1,2,3
order by 4
