//
//  ViewController_PrinterSubViewBitmap.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubView.h"

@interface ViewController_PrinterSubViewBarcode : ViewController_SubView<UIPickerViewDelegate, UIPickerViewDataSource>
{
    
    IBOutlet UILabel *_labelSelectedBarcodeType;
    IBOutlet UIPickerView *_pickerBarcodesList;
    IBOutlet UITextField *_textFieldBarcodeDataInput;
    IBOutlet UILabel *_labelSelectedBarcodeCode;
    
    IBOutlet UISegmentedControl *_segAlignment;
    IBOutlet UISegmentedControl *_segTextPosition;
    
    
}

- (IBAction)onChangeBarcode:(id)sender;
- (IBAction)onPrintBarcode:(id)sender;





@end
