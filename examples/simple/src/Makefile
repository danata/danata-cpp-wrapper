FC  := gfortran
FC_FLAGS := -DNUM=100 -DVAL=0.3

run: build
	./interpolate.exe

build: interpolate.F90
	${FC} ${FC_FLAGS} -o  interpolate.exe $^

clean:
	rm -f *.exe *.o *.mod
