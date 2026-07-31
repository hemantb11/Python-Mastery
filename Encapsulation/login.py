import random as r
import time


class userlogin:

    # Constructor
    def __init__(self):
        self.mobileno = ""
        self.__otp = None
        self.__attempts = 0

    # Check maximum attempts
    def check_attempts(self):
        if self.__attempts < 3:
            self.check_login()

    # Login Process
    def check_login(self):

        # Take mobile number from user
        self.mobileno = input("Enter the mobile no: ")

        # Validate mobile number
        if len(self.mobileno) and self.mobileno.isdigit():

            # Generate Random OTP
            self.__otp = r.randint(1000, 9999)

            # Store OTP sending time
            self.sendingtime = time.time()

            print("Sending Time :", self.sendingtime)
            print("Your OTP is :", self.__otp)

            # User enters OTP
            self.userotp = int(input("Enter the OTP : "))

            # Store OTP entered time
            self.currenttime = time.time()

            print("OTP Received At :", self.currenttime)

            # Check OTP Expiry (3 seconds)
            if self.currenttime - self.sendingtime > 3:
                print("OTP Expired")

                choice = input("Enter Choice (1. Resend OTP  2. Exit): ")

                # Resend OTP
                if choice == "1":
                    self.resendotp()
                    return

                return

            # OTP Verification
            if self.__otp == self.userotp:
                print("Welcome")
                return

            else:
                print("OTP Not Matched")

                # Increase Wrong Attempt Count
                self.__attempts += 1

                print(3 - self.__attempts, "Attempts Left!")

                # Maximum Attempts Reached
                if self.__attempts == 3:
                    print("Attempts are reached. Please try after some time.")
                    return

                # Retry Login
                self.check_attempts()

        else:
            print("Enter Digits Only")

    # Resend OTP Function
    def resendotp(self):
        self.check_login()


# Object Creation
obj = userlogin()

# Start Login Process
obj.check_login()
