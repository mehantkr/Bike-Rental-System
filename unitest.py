import unittest
from datetime import datetime, timedelta
from shop import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):

	def test_Bike_Rental_display_correct_stock(self):
		shop1 = BikeRental()
		shop2 = BikeRental(10)
		self.assertEqual(shop1.displaystock(), 0)
		self.assertEqual(shop2.displaystock(), 10)

	def test_rentBikeOnHourlyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)
		self.assertEqual(shop.rentBikeOnHourlyBasis(0), None)
		self.assertEqual(shop.rentBikeOnHourlyBasis(11), None) # 11>10
		# for valid input
		hour = datetime.now().hour
		self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, hour)

	def test_rentBikeOnDailyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)
		self.assertEqual(shop.rentBikeOnDailyBasis(0), None)
		self.assertIsNone(shop.rentBikeOnDailyBasis(11)) # 11>10
		# for valid input
		hour = datetime.now().hour
		self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)

	def test_rentBikeOnWeeklyBasis(self):
		shop = BikeRental(10)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(-1), None)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(0), None)
		self.assertEqual(shop.rentBikeOnWeeklyBasis(11), None) # 11>10
		# for valid input
		hour = datetime.now().hour
		self.assertEqual(shop.rentBikeOnWeeklyBasis(2).hour, hour)

#-------------------returnBike-----------------------------------
	def test_returnBike_for_invalid_rentalTime(self):
		returnbike = BikeRental(10)
		customer = Customer()

		# let the customer not rent a bike and try to return one
		request = customer.returnBike()
		self.assertIsNone(returnbike.returnBike(request))

		# manually check return function with error values
		self.assertIsNone(returnbike.returnBike(0,0,0))

	def test_returnBike_for_invalid_rentalBasis(self):
		shop = BikeRental(10)
		customer = Customer()

		# create (customers)
		# valid - rentalTime
		# valid - bikes
		# invalid - rentalBasis
		customer.rentalTime = datetime.now()
		customer.bikes = 3
		customer.rentalBasis = 7

		request = customer.returnBike()
		self.assertIsNone(shop.returnBike(request))

	def test_returnBike_for_invalid_numberOfBikes(self):

		shop = BikeRental(10)
		customer = Customer()

		# create (customers)
		# valid - rentalTime
		# invalid - bikes
		# valid - rentalBasis
		customer.rentalTime = datetime.now()
		customer.rentalBasis = 1
		customer.bikes = 0

		request = customer.returnBike()
		self.assertIsNone(shop.returnBike(request))


	def test_returnBike_for_valid_credentials(self):

        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()
        customer7 = Customer()
        customer8 = Customer()
        customer9 = Customer()

        #create valid rentalBasis for each customer
        customer1.rentalBasis = 1 # hourly
        customer2.rentalBasis = 2 # hourly
        customer3.rentalBasis = 3 # hourly
        customer4.rentalBasis = 4 # daily
        customer5.rentalBasis = 5 # daily
        customer6.rentalBasis = 6 # daily
        customer7.rentalBasis = 7 # weekly
        customer8.rentalBasis = 8 # weekly
        customer9.rentalBasis = 9 # weekly

        # create valid bikes for eah customers

        










unittest.main()