from django.db import models

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True)

class Suppliers(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 254)
    businessCode = models.CharField(max_length = 13)
    debt = models.DecimalField(max_digits = 10, decimal_places = 2)
    totalPurchase = models.DecimalField(max_digits = 10, decimal_places = 0)
    Status = models.BooleanField(default = True)
    note = models.TextField(blank = True)


class Products(models.Model):
    productName = models.CharField(max_length = 100)
    costOfSales = models.DecimalField(max_digits = 8, decimal_places = 0)
    price = models.DecimalField(max_digits = 8, decimal_places = 0)
    # entry_Date = models.CharField(max_length = 10)
    # out_of_Date = models.CharField(max_length = 10)
    Sales_Form = models.BooleanField(null = True)
    Sales_Link = models.BooleanField(null = True)
    Status = models.BooleanField(default = True)
    Location = models.CharField(max_length = 100)
    Product_Barcode= models.CharField(max_length = 20)

class Images(models.Model):
    path_image = models.CharField(max_length = 100)

class ProductGroup(models.Model):
    productGroupName= models.CharField(max_length = 100)
    # parentId

class StockTakes (models.Model):
    time = models.DateTimeField(auto_now_add = True)
    finishedAt = models.DateTimeField(auto_now_add = True)
    realAmount = models.DecimalField(max_digits = 8, decimal_places = 0)
    actualTotalValue = models.DecimalField(max_digits = 12, decimal_places = 0)
    amountDifferences= models.DecimalField(max_digits = 8, decimal_places = 0)
    increaseAmount= models.DecimalField(max_digits = 8, decimal_places = 0)
    increaseValue= models.DecimalField(max_digits = 8, decimal_places = 0)
    decreaseAmount= models.DecimalField(max_digits = 8, decimal_places = 0)
    decreaseValue= models.DecimalField(max_digits = 8, decimal_places = 0)
    note = models.TextField(blank = True)
    # status = models.BooleanField()

class Customers(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    birthday = models.CharField(max_length = 10)
    # gender
    taxIdentity = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    facebook = models.CharField(max_length = 100)
    status= models.BooleanField(default = True)
    note = models.TextField(blank = True)
    createAt = models.DateTimeField(auto_now_add = True)
    debt = models.DecimalField(max_digits = 8, decimal_places = 0)

class CustomerGroup(models.Model):
    customerGroupName = models.CharField(max_length = 100)
    # discount

class CustomerType(models.Model):
    productTypeName = models.CharField(max_length = 100)

class Invoices(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length = 10)
    # address
    # ward
    # district
    # seller
    # creator
    note = models.TextField(blank = True)
    totalAmount = models.DecimalField(max_digits = 12, decimal_places = 0)
    discount = models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_need_return = models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_returned= models.DecimalField(max_digits = 8, decimal_places = 0)
    status= models.BooleanField(default = True)
    # customerInfo

class Order(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    phone = models.CharField(max_length = 100)
    # address
    # ward
    # district
    # customer
    order_receiver = models.CharField(max_length = 100)
    # creator
    note = models.TextField(blank = True)
    total_amount= models.DecimalField(max_digits = 8, decimal_places = 0)
    discount= models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_need_return= models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_returned= models.DecimalField(max_digits = 8, decimal_places = 0)
    status = models.BooleanField(default = True)

class Return(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    # customerInfo
    # invoicesInfo
    # creator
    note = models.TextField(blank = True)
    total_amount= models.DecimalField(max_digits = 8, decimal_places = 0)
    discount= models.DecimalField(max_digits = 8, decimal_places = 0)
    total_after_discount= models.DecimalField(max_digits = 8, decimal_places = 0)
    fee_return= models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_need_return= models.DecimalField(max_digits = 8, decimal_places = 0)
    customer_returned= models.DecimalField(max_digits = 8, decimal_places = 0)
    status= models.BooleanField(default = True)
class PurchaseOrder(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    # supplierInfo
    # branchInfo   
    # importerInfo
    # creatorInfo    
    note = models.TextField(blank = True)
    total_quantity= models.DecimalField(max_digits = 8, decimal_places = 0)
    total_product= models.DecimalField(max_digits = 8, decimal_places = 0)
    total_amount= models.DecimalField(max_digits = 8, decimal_places = 0)
    discount= models.DecimalField(max_digits = 8, decimal_places = 0)
    need_return_supplier= models.DecimalField(max_digits = 8, decimal_places = 0)
    returned_supplier= models.DecimalField(max_digits = 8, decimal_places = 0)
    status= models.BooleanField(default = True)

class PurchaseReturn(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    # supplierInfo
    # branch
    # returner
    # creator
    # productInfo
    note = models.TextField(blank = True)
    total_quantity= models.DecimalField(max_digits = 8, decimal_places = 0)
    total_product= models.DecimalField(max_digits = 8, decimal_places = 0)
    total_amount= models.DecimalField(max_digits = 8, decimal_places = 0)
    discount= models.DecimalField(max_digits = 8, decimal_places = 0)
    supplier_need_return= models.DecimalField(max_digits = 8, decimal_places = 0)
    supplier_returned= models.DecimalField(max_digits = 8, decimal_places = 0)
    status= models.BooleanField(default = True)

class Payments(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    # PaymentType
    value = models.DecimalField(max_digits = 8, decimal_places = 0)
    # preparedBy
    # receiverInfo
    receiverName = models.CharField(max_length = 100)
    receivingAccount = models.CharField(max_length = 20)
    note = models.TextField(blank = True)
    accounting = models.BooleanField(default = True)

class Reciepts(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    # receiptType
    value= models.DecimalField(max_digits = 8, decimal_places = 0)
    # preparedBy
    # payerInfo
    payerName = models.CharField(max_length = 100)
    paymentAccount = models.CharField(max_length = 20)
    note = models.TextField(blank = True)
    accounting = models.BooleanField(default = True)

class PaymentType(models.Model):
    paymentTypeName = models.CharField(max_length = 100)
    note = models.TextField(blank = True)

class ReceiptType(models.Model):
    receiptTypeName = models.CharField(max_length = 100)
    note = models.TextField(blank = True)

class DamageItems(models.Model):
    total_amount = models.DecimalField(max_digits = 8, decimal_places = 0)
    time = models.DateTimeField(auto_now_add = True)
    # creator
    # productInfo
    # userGivenName
    note = models.TextField(blank = True)
    status= models.BooleanField(default = True)

