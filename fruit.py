# -*- coding: utf8 -*-   //utf8 대소문자 구분

class FruitSeller:
    def __init__(self, money, appleNum, price):
        self.myMoney=money
	self.numOfApple=appleNum
	self.APPLE_PRICE=price

    def saleApple(self, money):
        self.num = money / self.APPLE_PRICE
	self.numOfApple -=self.num
	self.myMoney += money
	return self.num

    def showSaleResult(self):
        print ("남은 사과: " , self.numOfApple)
        print ("판매 수익: " , self.myMoney)




class FruitBuyer:
    def __init__(self, money):
        self.myMoney=money
	self.numOfApple=0

    def buyApple(self, seller, money):
  	self.numOfApple += seller.saleApple(money);
    	self.myMoney-=money;

    def showBuyResult(self):
        print ("현재 잔액: " , self.myMoney)
        print ("사과 갯: " , self.numOfApple)



#class FruitSalesMain3: (클래스로 만들면 안된다.)
if __name__ == "__main__" :
	seller1 = FruitSeller(0, 30, 1500)
	seller2 = FruitSeller(0, 20, 1000)
	buyer = FruitBuyer(10000)

	buyer.buyApple(seller1, 4500)
	buyer.buyApple(seller2, 2000)


	print ("판매자 1의 현재 상황")
	seller1.showSaleResult()
	print ("판매자 2의 현재 상황")
	seller2.showSaleResult()
	print ("과일 구매자의 현재 상황")
	buyer.showBuyResult()



    	
