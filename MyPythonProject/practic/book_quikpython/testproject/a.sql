with a as (
select
a.fnumber,
decode(a.FBillStatus,1,'保存',2,'已提交',3,'审核','作废') 状态,
to_char(a.FBizDate,'YYYY/MM/DD') 业务日期,
c.FName_l2 业务类型,
a.FASSTACTNAME_L2 往来户,
a.FABSTRACTNAME 摘要,
to_char(chr(9)||d.fnumber) 物料编码,
d.fname_l2 物料名称,
b.FQUANTITY 数量,
b.FREALPRICE 实际单价,
b.FUNVERIFYAMOUNTLOCAL 未结算金额本位币,
b.FVERIFYAMOUNTLOCAL 已结算金额本位币,
to_char(chr(9)||b.FREMARK)	备注,
b.FRECIEVEPAYAMOUNTLOCAL 应收金额本位币
from
T_AR_OtherBill a
inner join T_AR_OtherBillentry b on a.fid=b.FParentID
left join T_SCM_BizType c on a.FBizTypeID=c.fid
left join T_BD_Material d on b.FMaterialID=d.fid
where  b.FUNVERIFYAMOUNTLOCAL<>0
and to_char(a.FBizDate,'YYYY/MM/DD')>='2020/12/25'
and to_char(a.FBizDate,'YYYY/MM/DD')<='2021/02/27'
and  a.FASSTACTNAME_L2='品胜数码旗舰店 （广东品胜电子股份有限公司）-电商'
and a.FBillStatus=3
),
b as (
select
a.fnumber,
sum(b.FUNVERIFYAMOUNTLOCAL) 未结算金额总计,
sum(b.FVERIFYAMOUNTLOCAL) 已结算金额总计,
sum(b.FRECIEVEPAYAMOUNTLOCAL) 应收金额总计
from
T_AR_OtherBill a
inner join T_AR_OtherBillentry b on a.fid=b.FParentID
left join T_SCM_BizType c on a.FBizTypeID=c.fid
left join T_BD_Material d on b.FMaterialID=d.fid
where  b.FUNVERIFYAMOUNTLOCAL<>0
and to_char(a.FBizDate,'YYYY/MM/DD')>='2020/12/25'
and to_char(a.FBizDate,'YYYY/MM/DD')<='2021/02/27'
and  a.FASSTACTNAME_L2='品胜数码旗舰店 （广东品胜电子股份有限公司）-电商'
and a.FBillStatus=3
group by a.fnumber
)
select
a.*,b.*
from a left join b on a.fnumber=b.fnumber