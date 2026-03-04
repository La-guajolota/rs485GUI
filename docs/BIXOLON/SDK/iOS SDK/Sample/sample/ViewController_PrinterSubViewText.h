//
//  ViewController_PrinterSubViewText.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubView.h"

@interface ViewController_PrinterSubViewText : ViewController_SubView
{
    IBOutlet UITextView *_textView_TextInput;
    IBOutlet UITextField *_textFieldScale;
}



- (IBAction)onCheckHealthExternal:(id)sender;
- (IBAction)onFeed:(id)sender;
- (IBAction)onCutPaper:(id)sender;
- (IBAction)onPrintNormal:(id)sender;
- (IBAction)onPrintBitmap:(id)sender;
- (IBAction)onPrintBarcode:(id)sender;

- (IBAction)onESCDefault:(id)sender;
- (IBAction)onESCAlignCenter:(id)sender;
- (IBAction)onESCAlignRight:(id)sender;

- (IBAction)onESCFontBold:(id)sender;
- (IBAction)onESCFontReverse:(id)sender;
- (IBAction)onESCFontUnderline:(id)sender;

- (IBAction)onESCScaleNormal:(id)sender;
- (IBAction)onESCScaleDoubleWH:(id)sender;
- (IBAction)onESCScaleDoubleW:(id)sender;
- (IBAction)onESCScaleDoubleH:(id)sender;
- (IBAction)onESCScaleVertical:(id)sender;
- (IBAction)onESCScaleHorizontal:(id)sender;


@end
