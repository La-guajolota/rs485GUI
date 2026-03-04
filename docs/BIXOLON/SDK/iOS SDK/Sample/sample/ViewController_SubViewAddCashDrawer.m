//
//  ViewController_SubView.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubViewAddCashDrawer.h"

@interface ViewController_SubViewAddCashDrawer ()
{
}
@end

@implementation ViewController_SubViewAddCashDrawer
@synthesize supportedModelList, registeredPrintersList;


- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

-(void) dealloc
{
    
    if(supportedModelList)
    {
        [supportedModelList release];
        supportedModelList = nil;
    }
    
    if(registeredPrintersList)
    {
        [registeredPrintersList release];
        registeredPrintersList = nil;
    }
    
    [_uiPickerSelectedPrinter release];
    [_uiButtonSelectPrinter release];
    
    [_uiLabel_modelName release];
    [_uiTextField_LDN release];
    
    [_uiSegmenteCtrl_PinLevel release];
    [_uiSegmenteCtrl_PinNumber release];
    [_uiSegmentedCtrl_InterfaceType release];
    
    [_uiSegmenteCtrl_PinNumber release];
    [_uiSegmenteCtrl_PinLevel release];
    [_uiTextField_PulseOnTime release];
    [_uiTextField_PulseOffTime release];
    [super dealloc];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    NSString* modelName = [supportedModelList objectAtIndex:0];
    if(modelName)
       [_uiLabel_modelName setText:modelName];
    else
        [_uiLabel_modelName setText:@"SRPCDW"];
}


- (BOOL)textFieldShouldReturn:(UITextField *)textField
{
    if([textField isFirstResponder])
        [textField resignFirstResponder];
    
    return YES;
}



-(void) parent:(ViewController_CashDrawer*)viewController
{
    _parentView = viewController;
}


- (IBAction)selectModel:(UIButton*)sender
{
    sender.hidden = YES;
    _uiPickerSelectedPrinter.delegate = self;
    _uiPickerSelectedPrinter.dataSource = self;
    
    [_uiPickerSelectedPrinter setShowsSelectionIndicator:YES];
    _uiPickerSelectedPrinter.hidden = NO;
//    _uiButtonSelectPrinter.hidden = YES;
}




- (IBAction)onButton_Test:(UIButton *)sender {
    NSLog(@"1111");
}

-(IBAction)onButton_OK:(UIButton*)sender
{
    
    if(_uiButtonSelectPrinter.titleLabel.text.length )
    {
        /* 기기 정보 업데이트 */
        UPOSCashDrawer* newDevice = [[UPOSCashDrawer alloc] init];
        
        //  정보 확인해서 대입
        newDevice.modelName    = _uiLabel_modelName.text;   //_uiButtonSelectPrinter.titleLabel.text;//@"SPP-R200II_2";
        newDevice.ldn          = _uiTextField_LDN.text;
        newDevice.selectedPrinterName = _uiButtonSelectPrinter.titleLabel.text;
        
        newDevice.pinNumber    = [NSNumber numberWithInteger:(_uiSegmenteCtrl_PinNumber.selectedSegmentIndex==0)? 2: 5];
        newDevice.pinLevel    = [NSNumber numberWithInteger:(_uiSegmenteCtrl_PinLevel.selectedSegmentIndex)];
        
        newDevice.pulseOnTime = [NSNumber numberWithInteger:[_uiTextField_PulseOnTime.text integerValue]];
        newDevice.pulseOffTime = [NSNumber numberWithInteger:[_uiTextField_PulseOffTime.text integerValue]];
        
            if([_parentView respondsToSelector:@selector(addCashDrawer:)])
            {
                [_parentView addCashDrawer:newDevice];
            }
         
        [newDevice release];
        
        ///////////////////////////////
    }
    //    -(void) updateDevice:(UIDevice*)device;
    
    /* 창 닫기 */
    NSLog(@"Popping back to this view controller!");
    // reset UI elements etc here
    //    [self performSegueWithIdentifier: @"SegueToScene1" sender:self];
    //    [출처] [Xcode] 뒤로가기 (되돌리기, unwind segue)|작성자 에몬
    if([[super parentViewController]respondsToSelector:@selector(dismissModalViewControllerAnimated:)])
    {
        [[super parentViewController] dismissModalViewControllerAnimated:YES];
    }
    else // if([[super parentViewController]respondsToSelector:@selector(dismissModalViewControllerAnimated:completion:)])
    {
        [[super presentingViewController] dismissViewControllerAnimated:YES completion:nil];
    }
    
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
    return [self.registeredPrintersList count];
}

- (NSString *)pickerView:(UIPickerView *)pickerView
             titleForRow:(NSInteger)row
            forComponent:(NSInteger)component
{
    return [self.registeredPrintersList objectAtIndex:row];
}


- (void)pickerView:(UIPickerView *)pickerView
      didSelectRow:(NSInteger)row
       inComponent:(NSInteger)component
{
    
    pickerView.hidden = YES;
    [_uiButtonSelectPrinter setTitle:[self.registeredPrintersList objectAtIndex:row] forState:UIControlStateNormal];
    _uiButtonSelectPrinter.hidden = NO;
    [_uiButtonSelectPrinter setAlpha:1.0];
    
}




@end
