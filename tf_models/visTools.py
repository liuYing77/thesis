import numpy as np
import matplotlib 
matplotlib.use('Agg') # To stop errors on goliath
import matplotlib.pyplot as plt

IMAGE_SIZE = 128

def show_preds(filename):
    """ Open a pickle file containing predictions and display them asking the
        user for input
    """
    dataset = np.load(filename)
    if 'ins' not in dataset.files or 'preds' not in dataset.files:
        raise Exception("Dataset missing ins or preds, may not be valid")
    ins = dataset['ins']
    preds = dataset['preds']
    assert ins.shape == preds.shape
    
    raise Exception("Function NOT Finished")

    cur_img = 0        

    while True:
        usr = input("Action (n/b/q):")
        if usr == 'n':
            pass
        elif usr == 'b':
            pass
        elif usr == 'q':
            break
        else:
            print("Unreccognised command:", usr)

def preds2png(filename, outdir):
    """ Given a saved file convert in/prediction pairs to pngs and save to
        outdir
        Preconditon: Assumes outdir exists and is writeable
                    filename is valid and readable
    """
     
    dataset = np.load(filename)
    if 'ins' not in dataset.files or 'preds' not in dataset.files:
        raise Exception("Dataset missing ins or preds, may not be valid")
    ins = dataset['ins']
    preds = dataset['preds']
    del dataset
    assert ins.shape == preds.shape
    
    batch_size = ins.shape[0]
    
    for i in xrange(batch_size):
        in_img = ins[i, :].reshape(IMAGE_SIZE, IMAGE_SIZE)
        pred_img = preds[i, :].reshape(IMAGE_SIZE, IMAGE_SIZE)

        plt.imshow(in_img, cmap='gray')  # Save input img
        plt.savefig(outdir + str(i) + "in.png")
    
        plt.imshow(pred_img, cmap='gray')  # save prediction
        plt.savefig(outdir + str(i) + "out.png")
        
        # When visualising weights can use something like
        # http://stackoverflow.com/questions/11775354/how-can-i-display-a-np-array-with-pylab-imshow
        # im = plt.imshow(arr, cmap='hot')
        # plt.colorbar(im, orientation='horizontal')
        # plt.show()        
        
        # multiple images in one figure
        # http://stackoverflow.com/questions/17111525/how-to-show-multiple-images-in-one-figure        
