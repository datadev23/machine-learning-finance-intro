import numpy as np

def test_run():
    a =	np.random.rand(5,3)
    print a
    print "values", a[0,1]
        
    a[0,0] = 1
    print a

    # update the first array
    a[:,3] =[1,2,3,4,5]

if __name__ == "__main__":
	test_run()
