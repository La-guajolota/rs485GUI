//
//  ViewController.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "UPOSPrinterController.h"
//#import "frmBixolonUPOS/UPOSPrinterController.h"

@interface ViewController_Printer : UIViewController <UPOSDeviceControlDelegate>
{
    IBOutlet    UITableView     *_tblPrinterList;
    IBOutlet    UIView          *_subView;
    
    IBOutlet UISegmentedControl *_segOpenClose;
    IBOutlet UISegmentedControl *_segClaimRelease;
    IBOutlet UISegmentedControl *_segEnableDisable;
    
    IBOutlet UISegmentedControl *_segFreezeEvents;
    IBOutlet UISegmentedControl *_segPowerNotify;
    IBOutlet UISegmentedControl *_segCartridgeNotify;
    IBOutlet UISegmentedControl *_segAsyncMode;
    IBOutlet UISegmentedControl *_segTransactionMode;
    
    IBOutlet UISegmentedControl *_segChangeView;
    
    IBOutlet UITextField        *_uiTextField_ResultCode;
    IBOutlet UITextField        *_uiTextField_ResultCodeExtended;
    IBOutlet UITextField        *_uiTextField_State;
    
    IBOutlet UITextField        *_uiTextField_ErrorLevel;
    IBOutlet UITextField        *_uiTextField_ErrorStation;
    IBOutlet UITextField        *_uiTextField_ErrorString;
    
    

    NSString                    *_historyEvents;
    
    
    UPOSPrinterController        *_uposPrinterController;
    UPOSPrinters                 *_deviceList;
    long                        _uposResult;
    
    NSArray                     *_subViewList;
}

//  Alert
- (void) message:(NSString *)message;
// Status Update
-(void) displayResult;


/********************************************************/
//  IBActions..
- (IBAction)changeSubViewValue:(UISegmentedControl *)sender;
- (IBAction)printerOpenClose:(UISegmentedControl *)sender;
- (IBAction)printerClaimRelease:(UISegmentedControl *)sender;
- (IBAction)printerEnableDisable:(UISegmentedControl *)sender;

- (IBAction)eventFreeze:(UISegmentedControl *)sender;
- (IBAction)powerNotifyOnOff:(UISegmentedControl *)sender;
- (IBAction)cartridgeNotifyOnOff:(UISegmentedControl *)sender;
- (IBAction)asyncModeOnOff:(UISegmentedControl *)sender;
- (IBAction)transactionONOff:(UISegmentedControl *)sender;
- (IBAction)onGetStatus:(id)sender;

- (IBAction)onButton_AddDevice:(id)sender;

/***********************************************************/
//  Call to Method for Printer for SubViews Menu
-(void) addPrinter : (UPOSPrinter*)printer;
-(void) checkHealth : (NSInteger) type;

-(void) printNormal : (NSString*) string;

-(void) printBarcode :(NSString *) BarcodeData
            symbology:(NSInteger) Symbology
               height:(NSInteger)Height
                width:(NSInteger)Width
            alignment:(NSInteger)Alignment
          textPostion:(NSInteger)textPosition;

-(void) printBitmap :(NSString *) fileName;
-(void) printBitmapWithImage :(UIImage *) image;

-(void) feed:(NSInteger) type;

-(void) cutPaper:(NSInteger)percentage;


-(void)StatusUpdateEvent:(NSNumber*) Status;
@end
