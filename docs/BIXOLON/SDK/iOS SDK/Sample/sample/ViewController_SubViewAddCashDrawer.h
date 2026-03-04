//
//  ViewController_SubView.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "UPOSDevices.h"
#import "ViewController_CashDrawer.h"


@interface ViewController_SubViewAddCashDrawer : UIViewController <UIPickerViewDelegate, UIPickerViewDataSource>
{
    ViewController_CashDrawer*     _parentView;
    
    IBOutlet    UITextField*        _uiTextField_LDN;
    
    IBOutlet    UISegmentedControl* _uiSegmentedCtrl_InterfaceType;
    
    IBOutlet    UIPickerView*       _uiPickerSelectedPrinter;
    IBOutlet    UIButton*           _uiButtonSelectPrinter;
    
    IBOutlet    UILabel*            _uiLabel_modelName;
    
    IBOutlet    UISegmentedControl* _uiSegmenteCtrl_PinNumber;
    IBOutlet    UISegmentedControl* _uiSegmenteCtrl_PinLevel;
    IBOutlet    UITextField*        _uiTextField_PulseOnTime;
    IBOutlet    UITextField*        _uiTextField_PulseOffTime;
}
@property (retain) NSArray*         supportedModelList;
@property (retain) NSArray*         registeredPrintersList;


- (IBAction)interfaceChanged:(UISegmentedControl *)sender;
- (IBAction)selectModel:(UIButton*)sender;


- (IBAction)onButton_Test:(UIButton *)sender;
- (IBAction)onButton_OK:(UIButton *)sender;

-(void) parent:(ViewController_CashDrawer*)viewController;
@end
