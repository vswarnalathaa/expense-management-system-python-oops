import matplotlib.pyplot as plt

def category_summary_chart(data):
    categories = data.keys()
    amount= data.values()
    plt.bar(categories,amount)
    plt.xlabel('Categories')
    plt.ylabel('Amount spend')
    plt.title('Amount spent by Category')
    plt.show()

def payment_method_summary_chart(data):
    payment_method = data.keys()
    amount = data.values()
    plt.bar(payment_method,amount)
    plt.xlabel('Payment Method')
    plt.ylabel('Amount spend')
    plt.title('Amount spent by Payment Method')
    plt.show()

def monthly_summary_chart(data):
    monthly = data.keys()
    amount = data.values()
    plt.plot(monthly,amount)
    plt.xlabel('Month')
    plt.ylabel('Amount spend')
    plt.title('Amount spent Monthly')
    plt.show()