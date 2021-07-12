all1: 
	gfortran -fallow-argument-mismatch velest/velest.f -o bin/velest 
all2: 
	gfortran -std=legacy velest/velest.f -o bin/velest 

clean: 
	rm -rf velest/*.o bin/velest 

