//
//  ViewController_SubView.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubViewAddSCR.h"

@interface ViewController_SubViewAddSCR ()
{
}
@end

@implementation ViewController_SubViewAddSCR
@synthesize supportedModelList;


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
    
    [_uiLabel_Address release];
    [_uiLabel_Port release];
    [_uiPickerModelName release];
    [_uiButtonSelectModel release];
    [super dealloc];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
}


- (BOOL)textFieldShouldReturn:(UITextField *)textField
{
    if([textField isFirstResponder])
        [textField resignFirstResponder];
    
    return YES;
}

-(void) parent:(ViewController_SCR*)viewController
{
    _parentView = viewController;
}
- (IBAction)interfaceChanged:(UISegmentedControl *)sender
{
    switch (sender.selectedSegmentIndex)
    {
        case 0:
        case 1:
            _uiLabel_Address.text = @"IP Address : ";
            _uiTextField_Port.enabled = YES;
            _uiTextField_Port.alpha = 1.0;
            _uiLabel_Port.alpha = 1.0;
            break;
        case 2:
        default:
        {
            _uiLabel_Address.text = @"MAC Address : ";
            _uiTextField_Port.enabled = NO;
            _uiTextField_Port.alpha = 0.4;
            _uiLabel_Port.alpha = 0.4;
        }
    }
    
}

- (IBAction)selectModel:(UIButton*)sender
{
    sender.hidden = YES;
    _uiPickerModelName.delegate = self;
    _uiPickerModelName.dataSource = self;
    
    [_uiPickerModelName setShowsSelectionIndicator:YES];
    _uiPickerModelName.hidden = NO;
//    _uiButtonSelectModel.hidden = YES;
}




- (IBAction)onButton_Test:(UIButton *)sender {
    NSLog(@"1111");
}

-(IBAction)onButton_OK:(UIButton*)sender
{
    
    if(_uiButtonSelectModel.titleLabel.text.length )
    {
        
        
        /* 기기 정보 업데이트 */
        
        UPOSSCR* newDevice = [[UPOSSCR alloc] init];
        
        //  정보 확인해서 대입
        newDevice.modelName    = _uiButtonSelectModel.titleLabel.text;//@"SPP-R200II_2";
        newDevice.ldn          = _uiTextField_LDN.text;
        
        //        newDevice.selectedP
        //        newDevice.devClass     = @"1234";
        
        NSInteger selectedIndex = 0;// _uiSegmentedCtrl_InterfaceType.selectedSegmentIndex;
        selectedIndex = MAX(_uiSegmentedCtrl_InterfaceType.selectedSegmentIndex<<1, MAX(_uiSegmentedCtrl_InterfaceType.selectedSegmentIndex, 1));
        
        newDevice.interfaceType= [NSNumber numberWithInteger:selectedIndex];  //[NSString stringWithFormat:@"%ld", (long)selectedIndex];//[NSString stringWithFormat: @"%d", 2^(_uiSegmentedCtrl_InterfaceType.selectedSegmentIndex) ];//@"4";
        
        
        newDevice.address      = _uiTextField_Address.text;//@"74:F0:7D:B0:02:0A";
        newDevice.port         = _uiTextField_Port.text;//@"";
        
        
        if([_parentView respondsToSelector:@selector(addSCR:)])
        {
            [_parentView addSCR:newDevice];
        }
        
        [newDevice release];
    }
    //    -(void) updateDevice:(UIDevice*)device;
    
    /* 창 닫기 */
    NSLog(@"Popping back to this view controller!");
    // reset UI elements etc here
    //    [self performSegueWithIdentifier: @"SegueToScene1" sender:self];
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
    return [self.supportedModelList count];
}

- (NSString *)pickerView:(UIPickerView *)pickerView
             titleForRow:(NSInteger)row
            forComponent:(NSInteger)component
{
    return [self.supportedModelList objectAtIndex:row];
}


- (void)pickerView:(UIPickerView *)pickerView
      didSelectRow:(NSInteger)row
       inComponent:(NSInteger)component
{
    
    pickerView.hidden = YES;
    [_uiButtonSelectModel setTitle:[self.supportedModelList objectAtIndex:row] forState:UIControlStateNormal];
    _uiButtonSelectModel.hidden = NO;
    [_uiButtonSelectModel setAlpha:1.0];
    
}




@end
