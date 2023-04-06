import argparse
import base64
import os

class File:
    
    def __init__(self,filepath:str,shielded:bool=False) -> None:

        self.filepath=filepath
        self.shielded=shielded
        self.path=os.path.dirname(self.filepath) 

    def __repr__(self) -> str:

        return f"File(filepath={self.filepath}, shielded={self.shielded})"

    # Converts the File content into base64 if the shielded parameter is False
    # and then it changes the shielded parameter into True
    def shield_file(self) -> None:

        if self.shielded == False:
            with open(self.filepath,"rb") as f:
                data=f.read()
                f.close()

            with open(self.filepath,"wb") as f:
                data=base64.b64encode(data)
                f.write(data)
                f.close()
            
            self.shielded=True

    # Converts the File content from base64 to normal if the shielded parameter is True
    # and then it changes the shielded parameter into False
    def unshield_file(self) -> None:

        try:
            if self.shielded == True:
                with open(self.filepath,"rb") as f:
                    data=f.read()
                    f.close()

                with open(self.filepath,"wb") as f:
                    data=base64.b64decode(data) 
                    f.write(data)
                    f.close()
                self.shielded=False

        except:
            return "File Is Not Shielded"

    # Property that returns True if the file is shielded and return False if file is not shielded
    @property
    def is_shielded(self):

        return self.shielded



class Parser:
    def __init__(self) -> None:
                
        self.parser=argparse.ArgumentParser()
        self.parser.add_argument("--lock","-lk",action="store_true")
        self.parser.add_argument("--unlock","-ulk",action="store_true")
        self.parser.add_argument("--file","-f",action="store")

    def run_parser(self):
        args=self.parser.parse_args()
        
        # 
        if args.file == None:
            print("Please enter valid file path by using: --file or -f")
            
        if os.path.isfile(args.file):

            if args.lock == True and args.unlock == False:
                file=File(filepath=args.file,shielded=False)
                file.shield_file()

            elif args.unlock == True and args.lock == False:
                file=File(filepath=args.file,shielded=True)
                file.unshield_file()

            elif args.lock == True and args.unlock == True:
                print("Can't Lock and Unlock at the same time.")

        else:
            print("Proper File Path Required.")


if __name__== "__main__":
    parser=Parser()
    parser.run_parser()