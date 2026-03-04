//
//  ViewController_PrinterSubViewText.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_PrinterSubViewBitmap.h"

@interface ViewController_PrinterSubViewBitmap ()

@end

@implementation ViewController_PrinterSubViewBitmap

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)onPrintBitmap:(id)sender
{
    
    
    //    NSString *path = [[NSBundle mainBundle] pathForResource:@"Sample" ofType:@"png"];
    //    [_parentView printBitmap:path]
  
    [_parentView printBitmapWithImage:_imageViewPreview.image];
    
}
- (void)dealloc
{
    [_imageViewPreview release];
    [super dealloc];
}
- (IBAction)onImageSelect:(id)sender {
    [self showImagePickerForSourceType:UIImagePickerControllerSourceTypePhotoLibrary];
}

- (IBAction)onCamera:(id)sender {
    [self showImagePickerForSourceType:UIImagePickerControllerSourceTypeCamera];
}



- (void)showImagePickerForSourceType:(UIImagePickerControllerSourceType)sourceType
{
//    if (imageView.isAnimating)
//    {
//        [imageView stopAnimating];
//    }
//    
//    if (capturedImages.count > 0)
//    {
//        [capturedImages removeAllObjects];
//    }
    
    UIImagePickerController *imagePickerController = [[UIImagePickerController alloc] init];
    imagePickerController.modalPresentationStyle = UIModalPresentationCurrentContext;
    imagePickerController.sourceType = sourceType;
    imagePickerController.delegate = self;
    
    if (sourceType == UIImagePickerControllerSourceTypeCamera)
    {
        /*
         The user wants to use the camera interface. Set up our custom overlay view for the camera.
         */
        imagePickerController.showsCameraControls = YES;//NO;
        
        /*
         Load the overlay view from the OverlayView nib file. Self is the File's Owner for the nib file, so the overlayView outlet is set to the main view in the nib. Pass that view to the image picker controller to use as its overlay view, and set self's reference to the view to nil.
         */
//        if(IS_iPhonePhone_5)
//        {
//            [[NSBundle mainBundle] loadNibNamed:@"OverlayView_4_0" owner:self options:nil];
//        }
//        else
//        {
//            [[NSBundle mainBundle] loadNibNamed:@"OverlayView_3_5" owner:self options:nil];
//        }
//        
//        overlayView.frame = _imagePickerController.cameraOverlayView.frame;
//        _imagePickerController.cameraOverlayView = overlayView;
//        overlayView = nil;
        
    }
    
    _imagePickerController = imagePickerController;

    [_parentView presentViewController:_imagePickerController animated:NO completion:nil];
}



#pragma mark - UIImagePickerControllerDelegate

// This method is called when an image has been chosen from the library or taken from the camera.
- (void)imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary *)info
{
#if 0
    
    _SbinLog(FLAG_LOG_SHOW_LEVEL1, @"+ imagePickerController\r\n" );
    UIImage	*image	= [info objectForKey:UIImagePickerControllerEditedImage];
    
    if( nil == image )
    {
        image	= [info objectForKey:UIImagePickerControllerOriginalImage];
    }
    
    imageView.image	= image;
    [getNaviViewController() dismissModalViewControllerAnimated:YES];
    
#else
    
//    [capturedImages addObject:image];
//    
//    if ([cameraTimer isValid])
//    {
//        return;
//    }
    
    UIImage *image = [info valueForKey:UIImagePickerControllerOriginalImage];
    _imageViewPreview.image = image;
    
    [self finishAndUpdate];
    

    
#endif
    
}


- (void)finishAndUpdate
{
    [_parentView dismissViewControllerAnimated:YES completion:NULL];
    
    
//    if ([capturedImages count] > 0)
//    {
//        if ([capturedImages count] == 1)
//        {
//            // Camera took a single picture.
//            [imageView setImage:[capturedImages objectAtIndex:0]];
//        }
//        else
//        {
//            // Camera took multiple pictures; use the list of images for animation.
//            imageView.animationImages = capturedImages;
//            imageView.animationDuration = 5.0;    // Show each captured photo for 5 seconds.
//            imageView.animationRepeatCount = 0;   // Animate forever (show all photos).
//            [imageView startAnimating];
//        }
//        
//        // To be ready to start again, clear the captured images array.
//        [capturedImages removeAllObjects];
//    }
//    
//    imagePickerController = nil;
}


- (void)imagePickerControllerDidCancel:(UIImagePickerController *)picker
{
    [_parentView dismissViewControllerAnimated:YES completion:NULL];
}



//////////////////////////////////
//  For Navication Controller

//- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
//{
//    // Return YES for supported orientations
//    return (interfaceOrientation == UIInterfaceOrientationPortraitUpsideDown);//UIInterfaceOrientationPortrait);
//}

- (NSUInteger)supportedInterfaceOrientations{
    return UIInterfaceOrientationMaskLandscape;
}

- (BOOL) shouldAutorotate
{
    return YES;//자동회전 허용
    //return NO; //자동회전 비허용
}


@end
