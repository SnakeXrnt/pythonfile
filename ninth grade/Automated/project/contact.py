
class Person:

    def __init__(self):
        self.name = None
        self.mail = None
        self.telfon = None



class Contact:

    def __init__(self,config):
        self.config = config
        self.contact_list = self.config.load_data(self.config.data_json_path)

    def show_contact(self):
        if len(self.contact_list) > 0 :
            print(f'Name\tPhone\tMail\n')
            for name,data in self.contact_list.items():
                print(f'{name}\t{data["phone"]}\t {data["mail"]}')
        else:
            msg = 'There is not contact yet'
            print(msg)
        input()

    def create_contact(self):

        print('Add New Contact\n')
        name = input('Name\t: \n')
        phone = input('Phone\t: ')
        mail = input('Mail\t: ')

        contact = {
        'phone' : phone,
        'mail' : mail
        }

        confirm = input('Are you sure? (y/n)')
        if confirm.lower() == 'y':
            self.contact_list[name] = contact
            self.config.save_data(self.contact_list,self.config.data_json_path)
            print('Contact has been saved')
        else:
            print('canceled')
        input(self.config.end_msg)

    def find_contact(self):
        self.user_input = input('Masukan nama kontak yang akan di cari : ')
        for name,data in self.contact_list.items():
            if self.user_input in name :
                print(f'{name}\t{data["phone"]}\t {data["mail"]}')
        input('Press [ENTER] untuk kembali ke menu utama ')

    def del_contact(self):
        self.user_input = input('Masukan nama kontak yang akan di Hapus : ')
        for name,data in self.contact_list.items():
            confirm = input('Are you sure? (y/n)')
            if confirm.lower() == 'y':

                if self.user_input in name :
                    del self.contact_list[self.user_input]
                    print('berhasil')
                else :
                    print('contact tidak di temukan')
            else:
                    print('cancelled')
        input('Press [ENTER] untuk kembali ke menu utama ')
