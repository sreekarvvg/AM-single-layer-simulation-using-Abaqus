      SUBROUTINE DFLUX(FLUX,SOL,KSTEP,KINC,TIME,NOEL,NPT,COORDS,
     1 JLTYP,TEMP,PRESS,SNAME)

      INCLUDE 'ABA_PARAM.INC'

      DIMENSION FLUX(2), TIME(2), COORDS(3)
      
      CHARACTER*80 SNAME

      X=COORDS(1)
      Y=COORDS(2)
      Z=COORDS(3)
      T=TIME(2)
      X0=0.0
      Y0=0.0
      Z0=0.0
      Q=2000
      R0=0.0075
      R0=R0**2
      PI=3.141593
      V=0.01

      XC=X0+V*T
      YC=Y0
      ZC=Z0
      ETTA=0.7

      FLUX(1)=0
      Q0=((3*Q*ETTA)/(PI*R0))*EXP((-3*((X-XC)**2+(Y-YC)**2))/R0)

      if (((X-XC)**2+(Y-YC)**2)<R0) then 
      FLUX(1)=Q0
      end if
      FLUX(2)=0.0
    

      RETURN
      END