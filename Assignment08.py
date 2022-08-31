# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# naomimartin, 08.29.2022, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'  # naomimartin: the string of the desired file name
lstOfProductObjects = []  # naomimartin: an empty list to which Product objects will be appended
choice_str = ""  # naomimartin: captures user input for selected menu choice
product_name = ""  # naomimartin: variable that holds user input for product name in main body of script
product_price = ""  # naomimartin: variable that holds user input for product price in main body of script
obj = None  # naomimartin: an empty object


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price

    methods:
        __str__(): overwrites default Python __str__() method and -> (str) of concatenated product name and price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 08.29.2022, Modified class to store data about a product
    """

    # -- Constructor -- #
    def __init__(self, product_name, product_price, list_of_product_objects):
        ''' The constructor method to initialize each object instance.

        :param product_name: (string) containing the name of the product
        :param product_price: (float) containing the price of the product
        '''
        self.__product_name_str = product_name
        self.__product_price_flt = product_price
        list_of_product_objects.append(self.__product_name_str + ", " + str(self.__product_price_flt))  # naomimartin:
        # append Product objects to list as soon as they are created. Show products in list as a character string for
        # looks

    # -- Methods -- #

    def __str__(self):  # naomimartin: overwrites the default Python __str__() method to show the user-inputted object
        # information, rather than the object type and its reference location
        ''' Overwrites the default Python __str__() method so that product name and price can be displayed when the
        product object is printed.

        :return: (string) containing the product name and its price
        '''
        return self.__product_name_str + ", " + str(self.__product_price_flt)

    # -- Properties -- #
    @property
    def product_name(self):  # naomimartin: provides access to the private attribute product_name
        ''' Getter function to indirectly access the product_name method.

        :return: (string) containing the product name
        '''
        return str(self.__product_name_str).title().strip()

    @product_name.setter
    def product_name(self, input_name):
        ''' Setter function to set the value of the product name.

        :param input_name: (string) containing user input for the product name
        :return: (string) containing the product name, returned in the getter function
        '''
        self.__product_name_str = input_name  # naomimartin: assigns the user input information input_name, obtained in
        # the IO class, to the object's product_name attribute

    @property
    def product_price(self):  # naomimartin: provides access to the private attribute product_price
        '''Getter function to indirectly access the product_price method.

        :return: (float) containing the product price
        '''
        return float(self.__product_price_flt).strip()

    @product_price.setter
    def product_price(self, input_price):
        ''' Setter function to set the value of the product price.

        :param input_price: (float) containing user input for the product price
        :return: (float) containing the product price, returned in the getter function
        '''
        self.__product_price_flt = input_price  # naomimartin: assigns the user input information input_price, obtained
        # in the IO class, to the object's product_price attribute


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        @staticmethod save_data_to_file(file_name, list_of_product_objects): saves each row of data in the specified
            list list_of_product_objects to the specified file_name

        @staticmethod read_data_from_file(file_name, list_of_product_objects): reads each row of data in specified
            file_name and -> (lst) list of product objects

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 08.29.2022, modified class to add methods
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        # naomimartin: selecting the "write" option when opening the file keeps old data and appends new data, since all
        # old data is loaded into the program at the beginning of the main body of the script, and therefore the new
        # list, which contains new information, overwrites the old list
        ''' Saves data from the specified list into the specified file.

        :param file_name: (string) containing the name of the file
        :param list_of_product_objects: (list) containing a list of product objects
        :return: (list) containing a list of product objects
        '''
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(row + "\n")
        file.close()
        return list_of_product_objects

    @staticmethod
    def read_data_from_file(file_name,list_of_product_objects):
        ''' Reads data from the specified file into the specified list.

        :param file_name: (string) containing the name of the file
        :param list_of_product_objects: (list) containing a list of product objects
        :return: (list) containing a list of product objects
        '''
        file = open(file_name, "r")
        all_data = file.readlines()  # naomimartin: .readlines() method reads all lines of the file into a list
        for row in all_data:  # naomimartin: appends all .readlines() output, stripped of the carriage return
            list_of_product_objects.append(row.strip())
        return list_of_product_objects


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks:

    methods:
        @staticmethod output_menu_choices(): displays a menu of options to the user
        @staticmethod input_menu_choice(): allows user to input desired menu choice
        @staticmethod output_current_products_in_list(list_of_product_objects): displays each row in the specified
            list_of_product_objects
        @staticmethod input_product_name() -> (string) containing name of product
        @staticmethod input_product_price() -> (float) containing price of product

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 08.29.2022, modified class to add methods
    """

    @staticmethod
    def output_menu_choices():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a new Product and Price
            2) View Current Products in List
            3) Save Product Data to File       
            4) Exit Program
            ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (str) containing user-inputted menu choice information
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_products_in_list(list_of_product_objects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_product_objects:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_product_name():
        ''' Receives user input for the name of product, and uses exception handling to ensure that only non-numerical
        values are given.

        :return: (string) containing the user input for the name of a product
        '''
        while True:
            try:
                input_name = input("Enter a Product Name: ").strip().title()
                if input_name.isnumeric():  # naomimartin: raises custom exception if input is numeric
                    raise Exception("Invalid input: product name must be a character string. Please try again. \n")
                else:
                    name = str(input_name)  # naomimartin: if exception is not raised, input_name assigned to name,
                    # which is returned in this function for later use in creating objects
                    break
            except Exception as e:
                print(e)
                continue
        return name

    @staticmethod
    def input_product_price():
        ''' Receives user input for the price of product, and uses exception handling to ensure that only numerical
        values are given.

        :return: (float) containing the user input for the price of a product
        '''
        while True:
            try:
                input_price = input("Enter a Product Price: ").strip().title()
                if input_price.isnumeric() == False:  # naomimartin: raises custom exception if input is not numeric
                    raise Exception("Invalid input: product price must be a number. Please try again. \n")
                else:
                    price = float(input_price)  # naomimartin: if exception is not raised, input_price assigned to
                    # price, which is returned in this function for later use in creating objects
                    break
            except Exception as e:
                print(e)
                continue
        return price


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName,lstOfProductObjects)

# Show user current data in the list of product objects
IO.output_current_products_in_list(lstOfProductObjects)

# Show user a menu of options
# Get user's menu option choice
while True:
    IO.output_menu_choices()
    choice_str = IO.input_menu_choice()

    if choice_str == "1":
        print("Add a new Product and Price\n")
        product_name = IO.input_product_name()  # naomimartin: tests to see if input is non-numeric
        product_price = IO.input_product_price()  # naomimartin: tests to see if input is numeric
        obj = Product(product_name, product_price,lstOfProductObjects)
        print("\nYour inputted product and price: ", obj)  # naomimartin: utilizes the __str__() method defined in the
        # Product class that was intended to overwrite the default Python __str__() method, so that information
        # pertaining to the object is printed
        print("\nProduct and Price successfully added to list! Returning to main menu... ")
    elif choice_str == "2":
        print("2) View Current Products in List\n")
        IO.output_current_products_in_list(lstOfProductObjects)
    elif choice_str == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Product data saved! Returning to main menu... ")
    elif choice_str == "4":
        print("Exiting program... ")
        break
    else:
        print("Invalid menu option: please try again.\n")  # naomimartin: loop re-executes if user does not input a
        # valid menu option.
        continue
