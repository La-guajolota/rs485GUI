//
//  ViewController_PrinterSubViewText.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_PrinterSubViewText.h"

@interface ViewController_PrinterSubViewText ()

@end

@implementation ViewController_PrinterSubViewText

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

- (IBAction)onCheckHealthExternal:(id)sender
{
    [_parentView checkHealth:UPOS_CH_EXTERNAL];
}

- (IBAction)onFeed:(id)sender
{
    [_parentView feed:1];
}

- (IBAction)onCutPaper:(id)sender
{
    [_parentView cutPaper:100];
    
}

- (IBAction)onPrintNormal:(id)sender
{
    
    if([_textView_TextInput isFirstResponder])
        [_textView_TextInput resignFirstResponder];
    [_parentView printNormal:_textView_TextInput.text];
    
//    [_parentView printNormal:@"\x1B|bC=======\x1B|!bC========\x1B|bC======\x1B|!bC====\r\n\r\n\r\n\r\n\r\n\x1B|100fP"];
//    
//    
//    [_parentView printNormal:@"\x1B|bC================================\r\n      OPOS T\x1B|!bCest \r\n\x1B|bCString    \r\n==============\x1B|!bC========\x1B|bC======\x1B|!bC====\r\n\x1B|100fP"];
//    [_parentView printNormal:@"\x1B|bC================================\r\n      OPOS T\x1B|!bCest \x1B|bCString    \r\n==============\x1B|!bC========\x1B|bC======\x1B|!bC====\r\n\x1B|100fP"];
//    
//    [_parentView printNormal:@"\x1B|bC1 \x1B|!bC2 \x1B|bC3 \x1B|!bC4 \x1B|bC5 \x1B|!bC6 \x1B|bC7 \x1B|!bC8 \x1B|bC9 \x1B|100fP"];
//    [_parentView printNormal:@"\x1B|bC1 \x1B|!bC2 \x1B|bC3 \x1B|!bC4 \r\n\x1B|bC5 \x1B|!bC6 \x1B|bC7 \x1B|!bC8 \x1B|bC9 \x1B|100fP"];
//    
//    
//    [_parentView printNormal:@"\x1B|uC1 \x1B|2uC2 \x1B|!uC3 \x1B|uC4 \x1B|2uC5 \x1B|!uC6 \x1B|uC7 \x1B|2uC8 \x1B|!uC9 \x1B|100fP"];
//    [_parentView printNormal:@"\x1B|uC1 \x1B|2uC2 \x1B|!uC3 \x1B|uC4 \r\n\x1B|2uC5 \x1B|!uC6 \x1B|uC7 \x1B|2uC8 \x1B|!uC9 \x1B|100fP"];
//    
//    
//    [_parentView printNormal:@"\x1B|rC1 \x1B|!rC2 \x1B|rC3 \x1B|!rC4 \x1B|rC5 \x1B|!rC6 \x1B|rC7 \x1B|!rC8 \x1B|rC9 \x1B|100fP"];
//    [_parentView printNormal:@"\x1B|rC1 \x1B|!rC2 \x1B|rC3 \x1B|!rC4 \r\n\x1B|rC5 \x1B|!rC6 \x1B|rC7 \x1B|!rC8 \x1B|rC9 \x1B|100fP"];
//
//    
//    
//    
//    NSString*   ESC = @"\x1B";
//    NSString* strOutputData = [NSString stringWithFormat:@"%@, "];
//    CString strOutputData;
//    strOutputData = ESC + "|cA" + ESC + "|2C" + ESC + "|bC" +"* Cafe Blue *" + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + "   3000 Spring Street, Rancho," + CRLF;
//    strOutputData = strOutputData + "   California 10093," + CRLF;
//    strOutputData = strOutputData + "   Tel) 858-519-3698 Fax) 3852" + CRLF + CRLF;
//    strOutputData = strOutputData + "Orange Juice                   5.00" + CRLF;
//    strOutputData = strOutputData + "6 Bufalo Wing                 24.00" + CRLF;
//    strOutputData = strOutputData + "Potato Skin                   12.00" + CRLF;
//    strOutputData = strOutputData + ESC + "|bC" + ESC + "|2rC" + "Subtotal                      41.00" + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + "Tax 6%                         2.46" + CRLF;
//    strOutputData = strOutputData + ESC + "|bC" + ESC + "|2rC" + "Member Discount                2.30" + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + ESC + "|bC" + "Cash                         100.00" + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + "Amt. Paid                     41.16" + CRLF;
//    strOutputData = strOutputData + ESC + "|bC" + ESC + "|2rC" + "Change Due                    58.84" + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + "Member Number : 452331949" + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|bC" + ESC + "|cA" + "Have a nice day !" + CRLF + CRLF + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + ESC + "|cA" + "Sale Date : " + strDate + CRLF;
//    strOutputData = strOutputData + ESC + "|N" + ESC + "|cA" + "Time : " + strTime + CRLF;
}

- (IBAction)onPrintBitmap:(id)sender
{
    NSString *path = [[NSBundle mainBundle] pathForResource:@"Sample" ofType:@"png"];
    [_parentView printBitmap:path];
    
}

- (IBAction)onPrintBarcode:(id)sender
{
//    const long PTR_BC_LEFT          = -1;
//    const long PTR_BCS_EAN13        = 104;  // = JAN 13 (added in 1.2)
//    const long PTR_BC_TEXT_BELOW    = -13;
    
    [_parentView printBarcode:@"1234567890123" symbology:104 height:100 width:200 alignment:-1 textPostion:PTR_BC_TEXT_BELOW];

    
}

- (void) addESCCommandAtTheTextInput:(NSString*)ESCCommand
{
    NSString*   ESC = @"\x1B";
    NSString* stringInput = _textView_TextInput.text;
    stringInput = [stringInput stringByAppendingFormat:@"%@%@", ESC, ESCCommand];
    _textView_TextInput.text = stringInput;
}

- (IBAction)onESCDefault:(id)sender {
    [self addESCCommandAtTheTextInput:@"|N"];
}

- (IBAction)onESCAlignCenter:(id)sender {
    [self addESCCommandAtTheTextInput:@"|cA"];
}

- (IBAction)onESCAlignRight:(id)sender {
    [self addESCCommandAtTheTextInput:@"|rA"];
}

- (IBAction)onESCFontBold:(id)sender {
    [self addESCCommandAtTheTextInput:@"|bC"];
}

- (IBAction)onESCFontReverse:(id)sender {
    [self addESCCommandAtTheTextInput:@"|rvC"];
}

- (IBAction)onESCFontUnderline:(id)sender {
    [self addESCCommandAtTheTextInput:@"|1uC"];
}

- (IBAction)onESCScaleNormal:(id)sender {
    [self addESCCommandAtTheTextInput:@"|1C"];
}

- (IBAction)onESCScaleDoubleWH:(id)sender {
    [self addESCCommandAtTheTextInput:@"|4C"];
}

- (IBAction)onESCScaleDoubleW:(id)sender {
    [self addESCCommandAtTheTextInput:@"|2C"];
}

- (IBAction)onESCScaleDoubleH:(id)sender {
    [self addESCCommandAtTheTextInput:@"|3C"];
}

- (IBAction)onESCScaleVertical:(id)sender {
    [self addESCCommandAtTheTextInput:[NSString stringWithFormat:@"|%dvC", [_textFieldScale.text intValue]]];
}

- (IBAction)onESCScaleHorizontal:(id)sender {
    [self addESCCommandAtTheTextInput:[NSString stringWithFormat:@"|%dhC", [_textFieldScale.text intValue]]];
}

- (void)dealloc
{
    [_textView_TextInput release];
    [_textFieldScale release];
    [super dealloc];
}
@end
