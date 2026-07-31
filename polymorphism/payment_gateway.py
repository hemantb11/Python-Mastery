class payment_gateway:

    # Common Method to Process Payment
    def payment_process(self, obj):

        # Start Payment Process
        print("Payment Process Started")

        # Check Whether pay() Method Exists
        if hasattr(obj, "pay"):

            # Call Child Class pay() Method
            obj.pay()

        else:

            # Display Error Message
            print("Method Not Found")

        # Payment Process Completed
        print("Payment Finally Done")