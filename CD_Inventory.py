#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AdamH, 2020-Mar-15, changed pseudocode to functional code
# AdamH, 2020-Mar-16, added docstrings and documentation
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstofCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        print_file: format the information in the CD to be stored to file in a CSV.
        print_legible: format the information to be printed in a legible manner. 
    """
    def __init__(self, cd_id, cd_title, cd_artist):
        try:
            self.cd_id = int(cd_id)
            self.cd_title = cd_title
            self.cd_artist = cd_artist
        except Exception as e:
            raise Exception('Error:\n' + str(e))
    
    def print_file(self):
        """Function to format the CD object to be saved into a CSV.

        Formats the information in the CD object such that each piece of data is seperated by a comma.
        
        Args:
            None.
            
        Returns:
            Formatted string to be saved as a CSV.
        """
        return '{},{},{}'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def print_legible(self):
        """Function to format the CD object to be printed and shown to the user

        Formats the information in the CD object such that each it is easily legible to the user when printed.
        
        Args:
            None.
            
        Returns:
            Formatted string to be printed.
        """
        return '{}\t{} (by:{})'.format(self.cd_id, self.cd_title, self.cd_artist)


# -- FILE PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to load data from a file.

        Reads data from a file, for each line instantiating a CD object, then adding
        each line to a table.
          
        Args:
            file_name: the name of the file to be read into memory.
            
        Returns:
            List of CD objects to be stored and used in the program.
        """
        table = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = CD(data[0], data[1], data[2])
                    table.append(row)
            return table
        except FileNotFoundError:
            print("The file {} could not be loaded.".format(file_name))
        
        
    def save_inventory(file_name, table):
        """Function to save data to a file.

        Iterates through the table stored in memory, and for each CD object
        in it, uses the print_file() method in the CD class to format the information
        into a CSV line.
          
        Args:
            file_name: the name of the file to be saved to.
            table: the name of the table of CD objects in memory.
            
        Returns:
            None.
        """
        try:            
            objFile = open(file_name, 'w')
            for row in table:
                data = row.print_file()
                objFile.write(data + '\n')
            objFile.close()
        except FileNotFoundError:
            print("The file {} could not be saved to.".format(file_name))
            
# -- MEMORY DATA PROCESSING -- #
class DataProcessor:
    """Processes and interacts with data in memory.

    properties: None

    methods:
        add_CD(CDInfo, table): -> None
        show_inventory(table): -> None
    """
    
    def add_CD(CDInfo, table):
        """Function to add a user-inputted line item to 2D data structure in memory

        Creates and adds a CD object to a 2D data structure (list of objects) after processing user input.
        
        Args:
            CDInfo (list): three item list inputted by the user to be used to create a CD object.
            table: the table in memory to save the CD object to.

        Returns:
            None.
        """
        cdID, title, artist = CDInfo
        try:
            cdID = int(cdID)
        except ValueError as E:
            print ('ID is not an integer! Error info:\n' + E)
        row = CD(cdID, title, artist)
        table.append(row)
        
    def show_inventory(table):
        """Function to print the table of CD objects stored in memory

        Prints each of the objects in the table stored in memory, using the method
        print_legible() in the CD class. 
          
        Args:
            table: the name of the table to be iterated through and printed.
            
        Returns:
            None.        
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row.print_legible())
        print('======================================')

# -- PRESENTATION (Input/Output) -- #
class IO:
    def print_menu():
        """Function to print the menu.

        Prints a formatted menu for the user, to present them their options and
        which keys to input for those options.
          
        Args:
            None.
            
        Returns:
            None.        
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
    def menu_choice():
        """Function to collect the user's menu choice.

        Collects the user's input in 'choice', and doesn't let the user input anything but the
        menu options that have functionality..
          
        Args:
            None.
            
        Returns:
            Choice, a single character string variable to be used for the if statement
            branches.        
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]:\n').lower().strip()
        return choice

    def input_CD():
        """Function to collect CD info.

        Prompts the user for an ID, CD title, and artist, then returns the tuple of those
        three inputs formatted for DataProcessor.add_cd() to use.
          
        Args:
            None.
            
        Returns:
            The three user inputs: ID, CD title, and Artist.        
        """
        try:
            intID = int(input('Enter ID: ').strip())
        except ValueError:
            print("The ID needs to be a number. Please try again.")
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, strArtist

# -- Main Body of Script -- #
lstOfCDObjects = FileIO.load_inventory(strFileName)
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled.\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        lstOfCDObjects = FileIO.load_inventory(strFileName)
        continue  # start loop back at top.
        
    elif strChoice == 'a':
        DataProcessor.add_CD(IO.input_CD(), lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 'i':        
        DataProcessor.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 's':
        DataProcessor.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            input('The inventory was successfully saved to file. Press [ENTER] to return to the menu.')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
    else:
        print('General Error')