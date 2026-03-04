//
//  ViewController_SubView.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "UPOSDevices.h"
#import "ViewController_SCR.h"

@interface ViewController_SubViewAddSCR : UIViewController <UIPickerViewDelegate, UIPickerViewDataSource>
{
    ViewController_SCR*     _parentView;
    IBOutlet    UILabel*            _uiLabel_Address;
    IBOutlet    UILabel *           _uiLabel_Port;
    
    IBOutlet    UITextField*        _uiTextField_LDN;
    
    IBOutlet    UISegmentedControl* _uiSegmentedCtrl_InterfaceType;
    IBOutlet    UITextField*        _uiTextField_Address;
    IBOutlet    UITextField*        _uiTextField_Port;
    IBOutlet    UIPickerView*       _uiPickerModelName;
    
    IBOutlet    UIButton*           _uiButtonSelectModel;
}
@property (retain) NSArray*         supportedModelList;


- (IBAction)interfaceChanged:(UISegmentedControl *)sender;
- (IBAction)selectModel:(UIButton*)sender;


- (IBAction)onButton_Test:(UIButton *)sender;
- (IBAction)onButton_OK:(UIButton *)sender;

-(void) parent:(ViewController_SCR*)viewController;
@end
