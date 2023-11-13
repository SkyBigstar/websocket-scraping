import re

a=" {SELECT Sum(INT(reports.costSummaries.costSummaryReport.parties.trades.materialCostSummary.cost)) FROM {JSONNAME} WHERE (reports.costSummaries.costSummaryReport.parties.trades.trade.id = 5 ) GROUP BY reports.costSummaries.costSummaryReport.parties.trades.trade.id HAVING Sum(INT(reports.costSummaries.costSummaryReport.parties.trades.materialCostSummary.cost))} "
if('{JSONNAME}' in a):
   a=a.replace("{JSONNAME}","(JSONNAME)")
matches = re.findall(r'\{(.*?)\}',a)
print(a)