import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your dataset loading logic
# customers_dataset_df = pd.read_csv('your_dataset.csv')
# Assuming `customers_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'customer_city': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasilia', 'Curitiba', 'Campinas', 'Porto Alegre', 'Salvador', 'Guarulhos', 'Sao Bernardo do Campo'],
    'customer_id': [15540, 6882, 2773, 2131, 1521, 1444, 1379, 1245, 1189, 938]
}
customers_dataset_df = pd.DataFrame(data)

# Grouping and sorting the data for the top 10 cities
top_cities = customers_dataset_df.groupby('customer_city')['customer_id'].nunique().sort_values(ascending=False).head(10)

# Plotting the bar chart
st.title('Top 10 Cities by Number of Unique Customer IDs')

fig, ax = plt.subplots()
top_cities.plot(kind='bar', colormap='magma', ax=ax)
ax.set_title('Top 10 Cities by Number of Unique Customer IDs')
ax.set_xlabel('City')
ax.set_ylabel('Number of Unique Customer IDs')

# Display the numeric data values on top of the bars
for index, value in enumerate(top_cities):
    ax.text(index, value + 100, str(value), ha='center', va='bottom', fontsize=10)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart displays the top 10 cities by the number of unique customer IDs. Sao Paulo has the highest number, significantly leading over the other cities.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your dataset loading logic
# customers_dataset_df = pd.read_csv('your_dataset.csv')
# Assuming `customers_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'customer_zip_code_prefix': ['01001', '01002', '01003', '01004', '01005', '01006', '01007', '01008', '01009', '01010'],
    'customer_id': [500, 450, 300, 275, 260, 240, 230, 220, 215, 200]
}
customers_dataset_df = pd.DataFrame(data)

# Grouping and sorting the data for the top 10 zip codes
top_zip = customers_dataset_df.groupby('customer_zip_code_prefix')['customer_id'].nunique().sort_values(ascending=False).head(10)

# Plotting the bar chart
st.title('Top 10 Zip Codes by Number of Unique Customer IDs')

fig, ax = plt.subplots()
top_zip.plot(kind='bar', colormap='magma', ax=ax)
ax.set_title('Top 10 Zip Codes by Number of Unique Customer IDs')
ax.set_xlabel('Zip Code')
ax.set_ylabel('Number of Unique Customer IDs')

# Display the numeric data values on top of the bars
for index, value in enumerate(top_zip):
    ax.text(index, value + 10, str(value), ha='center', va='bottom', fontsize=10)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart displays the top 10 zip codes by the number of unique customer IDs.
The zip code with the most unique customer IDs is leading with a significant margin.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_items_dataset_df = pd.read_csv('your_order_items_dataset.csv')
# Assuming `order_items_dataset_df` is already loaded as a Pandas DataFrame

# Sample data for demonstration
data = {
    'total_order_value': [100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 850, 900, 950, 1000, 1100]
}
order_items_dataset_df = pd.DataFrame(data)

# Plotting the histogram
st.title('Distribution of Total Order Value')

fig, ax = plt.subplots()
ax.hist(order_items_dataset_df['total_order_value'], bins=10, color='purple', edgecolor='black')
ax.set_xlabel('Total Order Value')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Total Order Value')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This histogram displays the distribution of the total order values. It shows the frequency of different total order value ranges.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_items_dataset_df = pd.read_csv('your_order_items_dataset.csv')
# Assuming `order_items_dataset_df` is already loaded as a Pandas DataFrame

# Sample data for demonstration
data = {
    'total_order_value': [100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400]
}
order_items_dataset_df = pd.DataFrame(data)

# Plotting the box plot
st.title('Box Plot of Total Order Value')

fig, ax = plt.subplots()
sns.boxplot(x=order_items_dataset_df['total_order_value'], ax=ax)
ax.set_xlabel('Total Order Value')
ax.set_title('Box Plot of Total Order Value')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This box plot shows the distribution of the total order values, highlighting the median, quartiles, and potential outliers in the dataset.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_payments_dataset_df = pd.read_csv('your_order_payments_dataset.csv')
# Assuming `order_payments_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'payment_sequential': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'order_id': [5000, 4000, 3500, 3200, 3000, 2500, 2000, 1800, 1600, 1500, 1400, 1300, 1200, 1100, 1000]
}
order_payments_dataset_df = pd.DataFrame(data)

# Grouping and sorting the data for the top 15 payment sequences
payseq = order_payments_dataset_df.groupby('payment_sequential')['order_id'].nunique().sort_values(ascending=False).head(15)

# Plotting the bar chart
st.title('Count of Payment Methods Chosen by Customers During Each Order')

fig, ax = plt.subplots()
payseq.plot(kind='bar', colormap='magma', ax=ax)
ax.set_title('Count of Payment Methods chosen by Customers during each order')
ax.set_xlabel('Count of Payment Methods')
ax.set_ylabel('Number of Unique Order IDs')

# Display the numeric data values on top of the bars
for index, value in enumerate(payseq):
    ax.text(index, value + 100, str(value), ha='center', va='bottom', fontsize=10)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart shows the distribution of how many different payment methods were chosen by customers in their orders.
The first payment method (sequential 1) has the highest count, indicating that most customers use a single payment method per order.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_payments_dataset_df = pd.read_csv('your_order_payments_dataset.csv')
# Assuming `order_payments_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'payment_type': ['credit_card', 'boleto', 'voucher', 'debit_card', 'credit_card', 'boleto', 'voucher', 'credit_card', 'debit_card']
}
order_payments_dataset_df = pd.DataFrame(data)

# Counting the occurrences of each payment type
paytype_count = order_payments_dataset_df['payment_type'].value_counts()

# Plotting the pie chart
st.title('Distribution of Payment Methods')

fig, ax = plt.subplots()
ax.pie(paytype_count, labels=paytype_count.index, autopct='%1.1f%%', colors=plt.cm.Set3.colors)
ax.set_title('Distribution of Payment Methods')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This pie chart shows the distribution of various payment methods used by customers.
Credit cards appear to be the most popular payment method, followed by boleto, voucher, and debit card.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_payments_dataset_df = pd.read_csv('your_order_payments_dataset.csv')
# Assuming `order_payments_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'payment_installments': [1, 2, 2, 3, 1, 1, 4, 3, 2, 1, 2, 3, 5, 1, 2],
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]
}
order_payments_dataset_df = pd.DataFrame(data)

# Grouping by payment installments and counting unique order IDs
payinstallment = order_payments_dataset_df.groupby('payment_installments')['order_id'].nunique().sort_values(ascending=False).head(10)

# Plotting the bar chart
st.title('Number of Installments Chosen for Each Order')

fig, ax = plt.subplots()
payinstallment.plot(kind='bar', colormap='magma', ax=ax)
ax.set_title('Number of Installments Chosen for Each Order')
ax.set_xlabel('Number of Installments')
ax.set_ylabel('Number of Unique Order IDs')

# Displaying numeric data values on top of the bars
for index, value in enumerate(payinstallment):
    ax.text(index, value + 0.1, str(value), ha='center', va='bottom', fontsize=10)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart illustrates the number of installments chosen for each order. 
It helps in understanding customer preferences regarding payment plans.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# order_reviews_dataset_df = pd.read_csv('your_order_reviews_dataset.csv')
# Assuming `order_reviews_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'review_score': [5, 4, 5, 3, 2, 5, 4, 4, 3, 2, 1, 5, 4, 3, 5]
}
order_reviews_dataset_df = pd.DataFrame(data)

# Counting the occurrences of each review score
reviewscore = order_reviews_dataset_df['review_score'].value_counts()

# Plotting the pie chart
st.title('Distribution of Customer Satisfaction with Purchase Experience')

fig, ax = plt.subplots()
ax.pie(reviewscore, labels=reviewscore.index, autopct='%1.1f%%', colors=plt.cm.Set3.colors)
ax.set_title('Distribution of Customer Satisfaction with Purchase Experience')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This pie chart represents the distribution of customer satisfaction scores based on their purchase experiences.
A higher percentage of scores indicates a greater level of satisfaction among customers.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# orders_dataset_df = pd.read_csv('your_orders_dataset.csv')
# Assuming `orders_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'order_purchase_timestamp': ['2024-01-01 12:00:00', '2024-01-02 13:00:00', '2024-01-03 14:00:00', 
                                  '2024-01-04 15:00:00', '2024-01-05 16:00:00'],
    'order_approved_at': ['2024-01-01 12:10:00', '2024-01-02 13:10:00', '2024-01-03 14:10:00', 
                          '2024-01-04 15:10:00', '2024-01-05 16:10:00'],
    'order_delivered_carrier_date': ['2024-01-01 14:00:00', '2024-01-02 14:00:00', '2024-01-03 14:00:00', 
                                      '2024-01-04 14:00:00', '2024-01-05 14:00:00'],
    'order_delivered_customer_date': ['2024-01-02 15:00:00', '2024-01-03 15:00:00', '2024-01-04 15:00:00', 
                                       '2024-01-05 15:00:00', '2024-01-06 15:00:00'],
    'order_estimated_delivery_date': ['2024-01-05 15:00:00', '2024-01-06 15:00:00', '2024-01-07 15:00:00', 
                                       '2024-01-08 15:00:00', '2024-01-09 15:00:00'],
    'order_status': ['delivered', 'shipped', 'canceled', 'delivered', 'pending']
}
orders_dataset_df = pd.DataFrame(data)

# Convert date columns to datetime
orders_dataset_df['order_purchase_timestamp'] = pd.to_datetime(orders_dataset_df['order_purchase_timestamp'], format='%Y-%m-%d %H:%M:%S')
orders_dataset_df['order_approved_at'] = pd.to_datetime(orders_dataset_df['order_approved_at'], format='%Y-%m-%d %H:%M:%S')
orders_dataset_df['order_delivered_carrier_date'] = pd.to_datetime(orders_dataset_df['order_delivered_carrier_date'], format='%Y-%m-%d %H:%M:%S')
orders_dataset_df['order_delivered_customer_date'] = pd.to_datetime(orders_dataset_df['order_delivered_customer_date'], format='%Y-%m-%d %H:%M:%S')
orders_dataset_df['order_estimated_delivery_date'] = pd.to_datetime(orders_dataset_df['order_estimated_delivery_date'], format='%Y-%m-%d %H:%M:%S')

# Counting the occurrences of each order status
orderstatus = orders_dataset_df['order_status'].value_counts()

# Plotting the pie chart
st.title('Distribution of Order Status')

fig, ax = plt.subplots()
ax.pie(orderstatus, labels=orderstatus.index, autopct='%1.1f%%', colors=plt.cm.Set3.colors)
ax.set_title('Distribution of Order Status')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This pie chart shows the distribution of different order statuses. 
Understanding the status distribution helps identify operational efficiencies and customer satisfaction.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# orders_dataset_df = pd.read_csv('your_orders_dataset.csv')
# Assuming `orders_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'order_purchase_timestamp': [
        '2024-01-01 12:00:00', '2024-01-02 13:00:00', '2024-01-03 14:00:00', 
        '2024-01-01 15:00:00', '2024-01-02 16:00:00', '2024-01-01 17:00:00', 
        '2024-01-02 18:00:00', '2024-01-03 19:00:00', '2024-01-03 20:00:00'
    ]
}
orders_dataset_df = pd.DataFrame(data)

# Convert purchase timestamp to datetime
orders_dataset_df['order_purchase_timestamp'] = pd.to_datetime(orders_dataset_df['order_purchase_timestamp'], format='%Y-%m-%d %H:%M:%S')

# Resampling the data to get the daily purchase count
purchase = orders_dataset_df.resample('D', on='order_purchase_timestamp').size()

# Plotting the line chart
st.title('Order Purchase Frequency')

fig, ax = plt.subplots()
ax.plot(purchase.index, purchase.values, linestyle='-')
ax.set_title('Order Purchase Frequency')
ax.set_xlabel('Date')
ax.set_ylabel('Frequency')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This line chart illustrates the frequency of orders purchased over time. 
Analyzing purchase frequency can help in understanding customer behavior and seasonality trends.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# products = pd.read_csv('your_products_dataset.csv')
# Assuming `products` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'product_category_name_english': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Electronics', 'Home', 'Furniture', 'Home', 'Clothing', 'Electronics', 'Furniture'
    ]
}
products = pd.DataFrame(data)

# Grouping by product category and counting unique products
product_counts = products.groupby('product_category_name_english')['product_id'].nunique().sort_values(ascending=False).reset_index().head(10)

# Plotting the bar chart
st.title('Number of Unique Products in Each Category')

fig, ax = plt.subplots()
ax.bar(product_counts['product_category_name_english'], product_counts['product_id'])
ax.set_xlabel('Product Category')
ax.set_ylabel('Number of Unique Products')
ax.set_title('Number of Unique Products in Each Category')
ax.set_xticklabels(product_counts['product_category_name_english'], rotation=45, ha='right')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart displays the number of unique products available in each category. 
Understanding the distribution of products across categories can help identify market trends and inventory management opportunities.
""")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# sellers_dataset_df = pd.read_csv('your_sellers_dataset.csv')
# Assuming `sellers_dataset_df` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'seller_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'seller_city': [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Curitiba',
        'São Paulo', 'Campinas', 'Porto Alegre', 'Salvador', 'Guarulhos',
        'São Bernardo do Campo', 'São Paulo', 'Curitiba', 'Rio de Janeiro', 'Belo Horizonte'
    ]
}
sellers_dataset_df = pd.DataFrame(data)

# Grouping by seller city and counting unique sellers
sellercity = sellers_dataset_df.groupby('seller_city')['seller_id'].nunique().sort_values(ascending=False).head(15)

# Plotting the bar chart
st.title('Top 15 Cities by Number of Unique Seller IDs')

fig, ax = plt.subplots()
sellercity.plot(kind='bar', ax=ax, colormap='magma')
ax.set_title('Top 15 Cities by Number of Unique Seller IDs')
ax.set_xlabel('City')
ax.set_ylabel('Number of Unique Seller IDs')

# Display the numeric data values on top of the bars
for index, value in enumerate(sellercity):
    ax.text(index, value + 0.1, str(value), ha='center', va='bottom')

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This bar chart shows the top cities ranked by the number of unique seller IDs. 
Understanding the seller distribution can help in analyzing market trends and opportunities for growth.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# data = pd.read_csv('your_data.csv')
# Assuming `data` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'customer_city': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Brasília',
                      'São Paulo', 'Campinas', 'Salvador', 'Porto Alegre', 'Fortaleza', 
                      'São Paulo', 'Curitiba', 'Rio de Janeiro', 'Belo Horizonte', 'Campinas'],
    'order_id': range(1, 15)
}
data = pd.DataFrame(data)

# Grouping by customer city and counting orders
topcities_orders = data.groupby("customer_city")["order_id"].count().reset_index().sort_values("order_id", ascending=False).head(10)

# Plotting the bar chart using Seaborn
st.title("Cities Generating the Most Orders (Top 10)")

fig, ax = plt.subplots()
sns.barplot(x="order_id", y="customer_city", data=topcities_orders, palette="viridis_r", ax=ax)

ax.set_xlabel("Number of Orders")
ax.set_ylabel("Cities")
ax.set_title("Cities Generating the Most Orders (Top 10)")

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This chart displays the top 10 cities generating the most orders. 
Analyzing order distribution across cities can help businesses understand where demand is highest.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulated dataset for demonstration, replace with your actual dataset loading logic
# data = pd.read_csv('your_data.csv')
# Assuming `data` is already loaded as a Pandas DataFrame

# Sample data creation for demonstration
data = {
    'customer_city': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Brasília',
                      'São Paulo', 'Campinas', 'Salvador', 'Porto Alegre', 'Fortaleza', 
                      'São Paulo', 'Curitiba', 'Rio de Janeiro', 'Belo Horizonte', 'Campinas'],
    'payment_value': [200, 150, 100, 80, 60, 300, 220, 180, 140, 90, 250, 130, 170, 110, 50]
}
data = pd.DataFrame(data)

# Grouping by customer city and summing payment values
topcities_revenue = data.groupby("customer_city")["payment_value"].sum().reset_index().sort_values("payment_value", ascending=False).head(10)

# Plotting the bar chart using Seaborn
st.title("Cities Generating the Highest Revenue")

fig, ax = plt.subplots()
sns.barplot(x="payment_value", y="customer_city", data=topcities_revenue, palette='viridis_r', ax=ax)

ax.set_xlabel("Total Revenue")
ax.set_ylabel("Cities")
ax.set_title("Cities Generating the Highest Revenue")

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This chart shows the top 10 cities generating the highest total revenue. 
Understanding revenue distribution can help businesses identify profitable markets.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration
# Replace this with your actual data loading logic
data = {
    'product_category_name_english': ['Electronics', 'Books', 'Clothing', 'Home', 'Toys', 'Sports', 'Grocery', 'Health', 'Beauty', 'Automotive'],
    'order_id': [150, 70, 90, 60, 30, 120, 110, 40, 80, 20]
}
data = pd.DataFrame(data)

# Streamlit app
st.title("Highest and Lowest Selling Product Categories by Number of Orders")

# Create subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(21, 7))

# Highest number of orders
toporders_productcat = data.groupby("product_category_name_english")["order_id"].nunique().reset_index().sort_values("order_id", ascending=False).head(10)
sns.barplot(x="order_id", y="product_category_name_english", data=toporders_productcat, palette='gnuplot_r', ax=ax[0])
ax[0].set_xlabel("Number of Orders")
ax[0].set_ylabel("Product Categories")
ax[0].set_title("Product Categories with the Highest Orders")

# Lowest number of orders
loworders_productcat = data.groupby("product_category_name_english")["order_id"].nunique().reset_index().sort_values("order_id", ascending=True).head(10)
sns.barplot(x="order_id", y="product_category_name_english", data=loworders_productcat, palette='gnuplot', ax=ax[1])
ax[1].set_xlabel("Number of Orders")
ax[1].set_ylabel("")
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Product Categories with the Lowest Orders")

# Title & adjustments
plt.suptitle("Highest and Lowest Selling Product Categories (in Number of Orders)")
plt.tight_layout(pad=1)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This visualization displays the highest and lowest selling product categories based on the number of orders. 
The left bar plot shows the categories with the most orders, while the right bar plot highlights those with the fewest.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration
# Replace this with your actual data loading logic
data = {
    'product_category_name_english': ['Electronics', 'Books', 'Clothing', 'Home', 'Toys', 'Sports', 'Grocery', 'Health', 'Beauty', 'Automotive'],
    'payment_value': [15000, 7000, 9000, 6000, 3000, 12000, 11000, 4000, 8000, 2000]
}
data = pd.DataFrame(data)

# Streamlit app
st.title("Highest and Lowest Revenue Generating Product Categories")

# Create subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(21, 7))

# Highest revenue generation
toprevenue_productcat = data.groupby("product_category_name_english")["payment_value"].sum().reset_index().sort_values("payment_value", ascending=False).head(10)
sns.barplot(x="payment_value", y="product_category_name_english", data=toprevenue_productcat, palette='gnuplot_r', ax=ax[0])
ax[0].set_xlabel("Total Revenue")
ax[0].set_ylabel("Product Categories")
ax[0].set_title("Product Categories Generating the Highest Revenue")

# Lowest revenue generation
lowrevenue_productcat = data.groupby("product_category_name_english")["payment_value"].sum().reset_index().sort_values("payment_value", ascending=True).head(10)
sns.barplot(x="payment_value", y="product_category_name_english", data=lowrevenue_productcat, palette='gnuplot', ax=ax[1])
ax[1].set_xlabel("Total Revenue")
ax[1].set_ylabel("")
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Product Categories Generating the Lowest Revenue")

# Title & adjustments
plt.suptitle("Highest and Lowest Selling Product Categories (in Revenue Generation)")
plt.tight_layout(pad=1)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This visualization displays the product categories generating the highest and lowest revenue. 
The left bar plot shows categories with the highest revenue, while the right plot highlights those with the lowest revenue.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data creation for demonstration
# Replace this with your actual data loading logic
# Example: Creating a sample heatmap data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hours = [f'{i}:00' for i in range(24)]
data = np.random.randint(0, 100, size=(7, 24))  # Random data for example
day_hour = pd.DataFrame(data, index=days, columns=hours)

# Streamlit app
st.title("Heatmap of Transactions Over the Hour by Day")

# Create the heatmap
plt.figure(figsize=(20, 5))
ax = sns.heatmap(day_hour, annot=True, fmt="d", cmap="OrRd")
ax.set_xlabel("Hour")
ax.set_ylabel("Day")
ax.set_title("Heatmap of Transactions Over the Hour by Day")

# Show the plot in Streamlit
st.pyplot(plt)

# Additional description or insights
st.write("""
This heatmap visualizes the number of transactions occurring at each hour of the day across different days of the week.
The values represent the frequency of transactions, with color intensity indicating the number of transactions.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration
# Replace this with your actual data loading logic
# Example: Creating a sample delivery time data
np.random.seed(42)
delivery_time_days = np.random.randint(1, 15, size=100)  # Random delivery time between 1 and 14 days
data = pd.DataFrame({'deliveryTime_Days': delivery_time_days})

# Streamlit app
st.title("Distribution of Delivery Time Across All Orders")

# Create the boxplot
plt.figure(figsize=(15, 5))
sns.boxplot(data=data['deliveryTime_Days'], orient='h', showfliers=False)
plt.xlabel("Number of Days")
plt.title('Distribution of Delivery Time Across All Orders')

# Show the plot in Streamlit
st.pyplot(plt)

# Additional description or insights
st.write("""
This boxplot visualizes the distribution of delivery times for all orders. 
The box represents the interquartile range, with the line inside indicating the median. 
Outliers have been excluded for a clearer view of the data.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration
# Replace this with your actual data loading logic
# Example: Creating a sample dataset
np.random.seed(42)
review_scores = np.random.randint(1, 6, size=100)  # Random review scores from 1 to 5
delivery_time_days = np.random.randint(1, 15, size=100)  # Random delivery time between 1 and 14 days
data = pd.DataFrame({'review_score': review_scores, 'deliveryTime_Days': delivery_time_days})

# Streamlit app
st.title("Delivery Time vs. Review Scores")

# Create the boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(x="review_score", y="deliveryTime_Days", data=data, showfliers=False, palette='viridis')
plt.xlabel("Review Score")
plt.ylabel("Delivery Time (in Days)")
plt.title("Delivery Time vs. Review Scores")

# Show the plot in Streamlit
st.pyplot(plt)

# Additional description or insights
st.write("""
This boxplot illustrates the relationship between customer review scores and delivery times.
Each box represents the interquartile range of delivery times for a given review score,
while the line inside the box indicates the median delivery time.
Outliers have been excluded for a clearer view of the data.
""")

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration
# Replace this with your actual data loading logic
# Example: Creating a sample dataset
np.random.seed(42)
categories = ['Electronics', 'Fashion', 'Home & Garden', 'Toys', 'Sports', 'Health', 'Automotive', 'Books', 'Beauty', 'Computers']
review_scores = np.random.randint(1, 6, size=100)  # Random review scores from 1 to 5
product_categories = np.random.choice(categories, size=100)  # Random categories
data = pd.DataFrame({'product_category_name_english': product_categories, 'review_score': review_scores})

# Streamlit app
st.title("Best and Worst Performing Product Categories Based on Review Scores")

# Calculate average review scores for each category
prodCat_TopReview = data.groupby("product_category_name_english")["review_score"].mean().reset_index().sort_values("review_score", ascending=False).head(10)
prodCat_BotReview = data.groupby("product_category_name_english")["review_score"].mean().reset_index().sort_values("review_score", ascending=True).head(10)

# Create the subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15.5, 4))

# Highest Rated Product Categories
sns.barplot(x="review_score", y="product_category_name_english", data=prodCat_TopReview, palette='plasma', ax=ax[0])
ax[0].set_xlabel("Average Review Score")
ax[0].set_ylabel("Product Categories")
ax[0].set_title("Highest Rated Product Categories")

# Lowest Rated Product Categories
sns.barplot(x="review_score", y="product_category_name_english", data=prodCat_BotReview, palette='plasma_r', ax=ax[1])
ax[1].set_xlabel("Average Review Score")
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Lowest Rated Product Categories")

# Title & adjustments
plt.suptitle("Best and Worst Performing Product Categories (in terms of Review Scores)")
plt.tight_layout(pad=1)

# Show the plot in Streamlit
st.pyplot(fig)

# Additional description or insights
st.write("""
This visualization illustrates the average review scores for product categories.
The left plot shows the highest-rated categories, while the right plot shows the lowest-rated ones.
Use this information to understand customer satisfaction across different product types.
""")

import time
import random
import folium
from folium import Marker
from folium.plugins import MarkerCluster

# Start timing the process
start = time.perf_counter()

# Create a base map centered around specified coordinates
m_1 = folium.Map(location=[-15, -55], tiles="cartodbpositron", zoom_start=3)

# Ensure rev_geo_customers is defined and has the necessary columns
# Sample random indices for customers
n_samples = 1000
if len(rev_geo_customers) >= n_samples:
    sample_idx = random.sample(rev_geo_customers.index.to_list(), k=n_samples)
    sample_df = rev_geo_customers.loc[sample_idx]

    # Create a marker cluster
    mc = MarkerCluster()
    for idx, row in sample_df.iterrows():
        mc.add_child(Marker([row["rep_lat"], row["rep_long"]]))
    m_1.add_child(mc)

    # Add title to the map
    title_html = '''
                 <h3 align="center" style="font-size:20px"><b>Show Where Customer Is</b></h3>
                 '''
    m_1.get_root().html.add_child(folium.Element(title_html))

    # Display the map
    display(m_1)
else:
    print("Not enough customers to sample.")

# Print the time consumed
print("The process consumes {:.2f} seconds.".format(time.perf_counter() - start))

import time
import random
import folium
import matplotlib.pyplot as plt
import numpy as np
from folium import Circle
from matplotlib.colors import rgb2hex
import pandas as pd

# Start timing the process
start = time.perf_counter()

# Create a base map
m_2 = folium.Map(location=[-15, -55], tiles="cartodbpositron", zoom_start=3)

# Define function to create color palette
def make_palette(n_samples, cmap):
    color_map = plt.get_cmap(cmap)
    palette = [rgb2hex(color_map(c)) for c in np.linspace(0.0, 1.0, n_samples)]
    return palette[n_samples:]

# Define function to categorize purchase prices
def color_producer(val):
    if val <= 45.9:
        return make_palette(2, "Blues")[0]
    elif val <= 86.9:
        return make_palette(2, "Blues")[1]
    elif val <= 137.8:
        return make_palette(1, "Wistia")[0]
    elif val <= 149.9:
        return make_palette(2, "Reds")[0]
    else:
        return make_palette(2, "Reds")[1]

# Sample data
n_samples = 1000
if len(purchase_price_df) < n_samples:
    n_samples = len(purchase_price_df)  # Adjust sample size if needed
sample_idx = random.sample(purchase_price_df.index.to_list(), k=n_samples)
sample_df = purchase_price_df.loc[sample_idx]

# Add bubbles to the map
for _, row in sample_df.iterrows():
    Circle(
        location=[row["rep_lat"], row["rep_long"]],
        radius=row["purchase_price"],
        color=color_producer(row["purchase_price"]),
        popup=f"Price: {row['purchase_price']:.2f}"  # More info in popup
    ).add_to(m_2)

# Function to add categorical legend
def add_categorical_legend(folium_map, title, colors, labels):
    if len(colors) != len(labels):
        raise ValueError("Colors and labels must have the same length.")
    legend_html = f"""
    <div id='maplegend' class='maplegend'>
      <div class='legend-title'>{title}</div>
      <div class='legend-scale'>
        <ul class='legend-labels'>
        {''.join(f"<li><span style='background:{color}'></span>{label}</li>" for label, color in zip(labels, colors))}
        </ul>
      </div>
    </div>
    """
    css = """<style type='text/css'> /* CSS for legend */ </style>"""  # (CSS omitted for brevity)
    folium_map.get_root().html.add_child(folium.Element(legend_html + css))
    return folium_map

# Prepare color_df for legend
color_df = pd.DataFrame(dict(
    purchase_price=["Very Low(<= 45.9)", "Low(<= 86.9)", "Middle(<= 137.8)", "High(<= 149.9)", "Very High(> 149.9)"],
    color=[make_palette(2, "Blues")[0], make_palette(2, "Blues")[1], make_palette(1, "Wistia")[0], make_palette(2, "Reds")[0], make_palette(2, "Reds")[1]]
))

# Add legend to the map
m_2 = add_categorical_legend(m_2, 'Purchase Price', color_df.color.tolist(), color_df.purchase_price.tolist())

# Add title to the map
title_html = '''<h3 align="center" style="font-size:20px"><b>Show Purchase Price<br>(n_samples=1,000)</b></h3>'''
m_2.get_root().html.add_child(folium.Element(title_html))

# Display the map
display(m_2)

# Check the time
print("The process consumes {:.2f} seconds.".format(time.perf_counter() - start))
