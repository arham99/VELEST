
Source of velet can be found in http://www.seg.ethz.ch/software/velest.html

code downloaded on 04/02/2019


Requeriments
------------

Install gfortran and devtools (make, gcc, etc) in your system, in debian/ubuntu you can do:

	sudo apt-get install build-essential gfortran

on fedora 

	sudo yum install gcc-gfortran

on Manjaro Linux

	sudo pamac install gcc-gfortran
	
after you can clone this repository by doing:

	git clone https://github.com/arham99/VELEST	


Compile
-------

Compile the code by running

	make all

The generated executable file is `bin/velest` 



# IMPORTANT NOTE : untuk non Linux user

Program VELEST ini sukses dikompilasi dan dijalankan pada sistem operasi Linux.
untuk windows user dapat menggunakan [Cygwin](https://cygwin.com/install.html), dengan menginstall package berikut ini:
- GCC
- gfortran
- make
- dll

NOTE : code pada VELEST bisa saja tidak bekerja dengan semestinya pada Cygwin, sehingga butuh di-edit secara manual pada source code (!!hati2)



### NOTE !!! 

Gunakan script `GADtoVelest.m` untuk membuat file .CNV, dokumentasi lebih lanjut pada [link](https://geophysical-info.blogspot.com/2019/08/tutorial-velest-3.html) ini

