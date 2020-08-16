# Nama : Aldhiya Rozak
# E-mail : aldhiya.rozak@gmail.com

from cli import *
from gui import *
def main():
	inp = input("Mau tampilan [cli/gui] : ").lower()
	if inp == "cli":
		tcli()
	elif inp == "gui":
		rt = tgui()
		rt.resizable(width=False, height=False)
		rt.mainloop()
if __name__ == '__main__':
	main()