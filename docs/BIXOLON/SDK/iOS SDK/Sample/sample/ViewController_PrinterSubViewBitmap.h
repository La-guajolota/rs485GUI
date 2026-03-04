//
//  ViewController_PrinterSubViewBitmap.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubView.h"

@interface ViewController_PrinterSubViewBitmap : ViewController_SubView <UIImagePickerControllerDelegate, UINavigationControllerDelegate>
{
    IBOutlet UIImageView *_imageViewPreview;
    UIImagePickerController* _imagePickerController;
    
    
}
- (IBAction)onImageSelect:(id)sender;
- (IBAction)onCamera:(id)sender;
- (IBAction)onPrintBitmap:(id)sender;


@end
