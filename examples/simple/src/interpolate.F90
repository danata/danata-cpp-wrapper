program interpolate

	implicit none

	real, parameter :: PI = 4.0*atan(1.0)
	real, allocatable, dimension(:) :: x
	real, allocatable, dimension(:) :: y
	integer i

	allocate(x(0:NUM))
	allocate(y(0:NUM))

	do i = 0, NUM
		x(i) = 2.0*PI*i/real(NUM)
		y(i) = sin(x(i))
	end do

	if ( (VAL < 0) .OR. (VAL > 2) ) then
		print *, 'Input value should be between 0 and 2, but ', VAL
		stop -1
	end if 

	print *, 'Interpolation value of SIN(',VAL,'* PI ) = ', interp(x, y, VAL*PI)

	deallocate(x)
	deallocate(y)

contains

real function interp(x, y, xp) result (yp)
	real, intent(in), dimension(:) :: x, y
	real, intent(in) :: xp

	yp = 0.0
	if ( size(x) .NE. size(y) ) then
		print *, 'Input array size mismatch'
		stop -1
	else
		do i = 2, size(x)
			if ( x(i)>xp ) then
				yp = y(i-1) + (xp - x(i-1)) * (y(i) - y(i-1)) / (x(i) - x(i-1))
				return
			end if 
		end do
	end if
end function


end program

