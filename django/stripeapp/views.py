from rest_framework.decorators import APIView 
from rest_framework.response import Response
from rest_framework import status
import stripe


stripe.api_key  ='sk_test_51M3JKiSFBSttbagxZMsqBiMlalG3nhVgnpUv5gfTQ0W2xeK6AKf7R0rftsSBvginFTddYtDydbf8Tk5LVtm5SCE6001YWHzvKh'

class StripeView(APIView):

    def post(self,request):

        test_payment_intent = stripe.PaymentIntent.create(
            amount=1000, currency='pln', 
            payment_method_types=['card'],
            receipt_email='test@example.com')
        return Response(status=status.HTTP_200_OK, data=test_payment_intent)

    def post(self,request):
        data = request.data
        email = data['email']
        payment_method_id = data['payment_method_id']
        msg = ''
        # checking if customer with provided email already exists
        customer_data = stripe.Customer.list(email=email).data   
        
        # if the array is empty it means the email has not been used yet  
        if len(customer_data) == 0:
            # creating customer
            customer = stripe.Customer.create(
            email=email, payment_method=payment_method_id,
            invoice_settings={
            'default_payment_method': payment_method_id
            })
        else:
            customer = customer_data[0]
            msg = "Customer already existed."

        stripe.PaymentIntent.create(
            customer=customer, 
            payment_method=payment_method_id,  
            currency='INR', 
            amount=999,
            confirm=True) 

        stripe.Subscription.create(
            customer=customer,
            items=[
            {
            'price': 'price_1M3MBdSFBSttbagxrJ9JNJRJ' 
            }
            ]
        )

        
        return Response(status=status.HTTP_200_OK, 
        data={
            'message': 'Success', 
            'data': {'customer_id': customer.id},
            'msg': msg   
        })                                                        