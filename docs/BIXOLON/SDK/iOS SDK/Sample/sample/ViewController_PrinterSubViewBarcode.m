//
//  ViewController_PrinterSubViewText.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_PrinterSubViewBarcode.h"
typedef struct barcodeType
{
    NSInteger       _code;
    NSString*        _name;
} _BAR_TYPE;

_BAR_TYPE barcodeTypes[] =
{
    {PTR_BCS_UPCA, @"PTR_BCS_UPCA"},
    {PTR_BCS_UPCE, @"PTR_BCS_UPCE"},
    {PTR_BCS_EAN8, @"PTR_BCS_EAN8"},
    {PTR_BCS_JAN13, @"PTR_BCS_JAN13"},
    {PTR_BCS_EAN13, @"PTR_BCS_EAN13"},
    {PTR_BCS_TF, @"PTR_BCS_TF"},
    {PTR_BCS_ITF, @"PTR_BCS_ITF"},
    {PTR_BCS_Codabar, @"PTR_BCS_Codabar"},
    {PTR_BCS_Code39, @"PTR_BCS_Code39"},
    {PTR_BCS_Code93, @"PTR_BCS_Code93"},
    {PTR_BCS_UPCA, @"PTR_BCS_UPCA"},
    {PTR_BCS_Code128, @"PTR_BCS_Code128"},
    {PTR_BCS_UPCA_S, @"PTR_BCS_UPCA_S"},
    {PTR_BCS_UPCE_S, @"PTR_BCS_UPCE_S"},
    {PTR_BCS_UPCD1, @"PTR_BCS_UPCD1"},
    {PTR_BCS_UPCD2, @"PTR_BCS_UPCD2"},
    {PTR_BCS_UPCD3, @"PTR_BCS_UPCD3"},
    {PTR_BCS_UPCD4, @"PTR_BCS_UPCD4"},
    {PTR_BCS_UPCD5, @"PTR_BCS_UPCD5"},
    {PTR_BCS_EAN8_S, @"PTR_BCS_EAN8_S"},
    {PTR_BCS_EAN13_S, @"PTR_BCS_EAN13_S"},
    {PTR_BCS_EAN128, @"PTR_BCS_EAN128"},
    {PTR_BCS_Code128_Parsed, @"PTR_BCS_Code128_Parsed"},
    {PTR_BCS_RSS14, @"PTR_BCS_RSS14"},
    {PTR_BCS_RSS_EXPANDED, @"PTR_BCS_RSS_EXPANDED"},
    {PTR_BCS_GS1DATABAR, @"PTR_BCS_GS1DATABAR"},
    {PTR_BCS_GS1DATABAR_E, @"PTR_BCS_GS1DATABAR_E"},
    {PTR_BCS_GS1DATABAR_S, @"PTR_BCS_GS1DATABAR_S"},
    {PTR_BCS_GS1DATABAR_E_S, @"PTR_BCS_GS1DATABAR_E_S"},
    {PTR_BCS_PDF417, @"PTR_BCS_PDF417"},
    {PTR_BCS_MAXICODE, @"PTR_BCS_MAXICODE"},
    {PTR_BCS_DATAMATRIX, @"PTR_BCS_DATAMATRIX"},
    {PTR_BCS_QRCODE, @"PTR_BCS_QRCODE"},
    {PTR_BCS_UQRCODE, @"PTR_BCS_UQRCODE"},
    {PTR_BCS_AZTEC, @"PTR_BCS_AZTEC"},
    {PTR_BCS_UPDF417, @"PTR_BCS_UPDF417"},
    {PTR_BCS_OTHER, @"PTR_BCS_OTHER"},
};



@interface ViewController_PrinterSubViewBarcode ()

@end

@implementation ViewController_PrinterSubViewBarcode

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
    
    
    _pickerBarcodesList.hidden = YES;
    [_labelSelectedBarcodeCode setText:[NSString stringWithFormat:@"%d", (int)barcodeTypes[4]._code]];
    [_labelSelectedBarcodeType setText:barcodeTypes[4]._name];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)dealloc
{
    [_labelSelectedBarcodeType release];
    [_pickerBarcodesList release];
    [_textFieldBarcodeDataInput release];
    [_labelSelectedBarcodeCode release];
    [_segAlignment release];
    [_segTextPosition release];
    [super dealloc];
}



- (IBAction)onChangeBarcode:(id)sender
{
    
    _labelSelectedBarcodeCode.hidden = YES;
    _labelSelectedBarcodeType.hidden = YES;
    _pickerBarcodesList.hidden = NO;
    _pickerBarcodesList.delegate = self;
    _pickerBarcodesList.dataSource = self;
    
//    sender.hidden = YES;
//    _uiPickerModelName.delegate = self;
//    _uiPickerModelName.dataSource = self;
//    
//    [_uiPickerModelName setShowsSelectionIndicator:YES];
//    _uiPickerModelName.hidden = NO;
//    
//    _uiButtonSelectModel.hidden = YES;
//    _uiLabel_SelectedModel.hidden = YES;
//    _uiTextField_LDN.hidden = YES;  //  다른 UI랑 겹치지 않기 위해서 숨김.
}

- (IBAction)onPrintBarcode:(id)sender {
    [_parentView printBarcode:_textFieldBarcodeDataInput.text symbology:[_labelSelectedBarcodeCode.text integerValue] height:100 width:200 alignment:(PTR_BC_LEFT-_segAlignment.selectedSegmentIndex) textPostion:(PTR_BC_TEXT_NONE-_segTextPosition.selectedSegmentIndex)];
    
    
//    [_parentView printBarcode:@"1234567890123" symbology:104 height:100 width:200 alignment:-1 textPostion:PTR_BC_TEXT_BELOW];
}




#pragma mark UIPickerView delegate methods

- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView
{
    return 1;
}

- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component
{
    //  Item  갯수
    //    return sizeof(_models)/sizeof(_models[0]);
    return (sizeof(barcodeTypes)/sizeof(barcodeTypes[0]));
}

- (NSString *)pickerView:(UIPickerView *)pickerView
             titleForRow:(NSInteger)row
            forComponent:(NSInteger)component
{
    //  Item 이름
    //    return @"test";//[NSString stringWithFormat:@"test-%d", row];
    //    return _models[row];
    return barcodeTypes[row]._name;
}


- (void)pickerView:(UIPickerView *)pickerView
      didSelectRow:(NSInteger)row
       inComponent:(NSInteger)component
{
    
    pickerView.hidden = YES;
    
    _labelSelectedBarcodeCode.hidden = NO;
    _labelSelectedBarcodeType.hidden = NO;
    
    [_labelSelectedBarcodeType setText:barcodeTypes[row]._name];
    [_labelSelectedBarcodeCode setText:[NSString stringWithFormat:@"%d", (int)barcodeTypes[row]._code]];
}

@end
