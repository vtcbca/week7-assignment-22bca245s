import csv
with open('E:\\product_selling.csv','w',newline='') as file:
    csv_w=csv.writer(file)
    columns=['Prod_No', 'Prod_Name',' Jan','Feb','Mar','Apr','May','Jun']
    csv_w.writerow(columns)
    
with open('E:\\product_selling.csv','a',newline='') as f :
    csv_w=csv.writer(f)
    records=[]
    for i in range(6):
        Prod_No=int(input("Enter product number:"))
        Prod_Name=input("Enter Product Name:")
        Jan=int(input("Enter product sales in January:"))
        Feb=int(input("Enter product sales in February:"))
        Mar=int(input("Enter product sales in March:"))
        Apr=int(input("Enter product sales in APril:"))
        May=int(input("Enter product sales in May:"))
        Jun=int(input("Enter product sales in June:"))
        t=( Prod_No,Prod_Name,Jan,Feb,Mar,Apr,May,Jun)
        records.append(t)
    csv_w.writerows(records)

import pandas as pd

print("\n2. Create dataframe:-")
df=pd.read_csv('E:\\product_selling.csv')
df

print("\n3. Change Column Name Product No, Product Name, January, February, March, April, May, June:-")
df.rename(columns={'Prod_No':'Product No','Prod_Name':'Product Name',' Jan':'January','Feb':'February','Mar':'March','Apr':'April','May':'May','Jun':'June'},inplace=True)
df

print("\n4. Add column Total Sell to count total of all month and Average Sell:-")
total_sell=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
df['Total']=total_sell
avg_sell=df['Total']/6
df['Average']=avg_sell
df

print("\n7. Print first 5 row:-")
df.head()

print("\n8. Print Last 5 row:")
df.tail()

print("\n9. Print row 6 to 10:-")
df.loc[5:9]

print("\n10. Print only product name:-")
print(df["Product Name"])

print("\n11. Print sell of January month with product id and product name:-")
print(df[["Product No","Product Name","January"]])

print("\n12. Print only those product id , product name where january sell is > 5000 and February sell is >8000")
print(df[(df["January"]>5000)& (df["February"]>8000)][["Product No","Product Name"]])

print("\n13. Print record in sorting order of Product name:")
df["Product Name"].sort_values()

print("\n14. Display only odd index number column record:")
df.iloc[1::2]

print("\n15. Display alternate row:-")
df.iloc[::2]


