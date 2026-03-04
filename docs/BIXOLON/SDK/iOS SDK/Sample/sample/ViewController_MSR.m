
//
//  ViewController.m
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_MSR.h"

#import "ViewController_SubViewAddMSR.h"
@interface ViewController_MSR ()
{
//    ViewController_SubView*   _subViewPrinter_Text;
    
    UIPopoverController*                         _popOver;
ViewController_SubViewAddMSR*            _subViewAddMSR;
}
@end

@implementation ViewController_MSR

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    _uposMSRController =   [UPOSMSRController new];
    _uposMSRController.delegate = self;
//    _uposMSRController.CharacterSet = 437;
    _deviceList =   [_uposMSRController getRegisteredDevice];
    
//    NSLog(@"support Device List : %@", [_uposMSRController getSupportDevices]);
    while([_deviceList getList].count)
    {
        [_deviceList removeDevice:[[_deviceList getList] lastObject]];
    }
    [_tblMSRList reloadData];
    
    [self initialize_SubViews];
}

- (void)dealloc
{
    [_uposMSRController release];
    [_segOpenClose release];
    [_segClaimRelease release];
    [_segEnableDisable release];
    
    
//    _subViewList
    
    for(id p in _subViewList)
    {
        [p release];
    }
    [_subViewList release];
 
    [_subViewAddMSR release];
    
    [_uiTextField_ResultCode release];
    [_uiTextField_ResultCodeExtended release];
    [_uiTextField_State release];
    [_uiTextField_ErrorLevel release];
    [_uiTextField_ErrorStation release];
    [_uiTextField_ErrorString release];
    [_uiTextViewHistory release];
    [super dealloc];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(void) initialize_SubViews
{
    //  _subView 들을 표시해주는 서브뷰 껍데기가 명확히 보이도록 테두리 삽입.
    _uiTextViewHistory.layer.borderWidth = 1.0;
    _uiTextViewHistory.layer.borderColor = [[UIColor darkGrayColor] CGColor];
    _uiTextViewHistory.layer.cornerRadius= 8;
    
    
    _uiTextViewHistory.text = @"";
    _uiTextViewHistory.editable = NO;
    
    
    UIStoryboard *storyBoard;
    if(_IS_IPAD)
    {
        // UIStoryboard 생성
        storyBoard = [UIStoryboard storyboardWithName:@"Main_iPad" bundle:nil];
    }
    else
    {
        // UIStoryboard 생성
        storyBoard = [UIStoryboard storyboardWithName:@"Main_iPhone" bundle:nil];
    }
    
    // 생성한 UIStoryboard에서  initial view controller를 가져온다.
    _subViewAddMSR =  [storyBoard instantiateViewControllerWithIdentifier:@"ViewController_SubViewAddMSR"];
    [_subViewAddMSR retain];
}

-(BOOL) doChangeSubView:(UIView*)view
{
    if(view == nil)
        return NO;
//    NSLog(@"userInteractionsEnabled : %d", _subView.userInteractionEnabled);
    [view setFrame:CGRectMake(0,0, _subView.frame.size.width, _subView.frame.size.height)];
    _subView.userInteractionEnabled = YES;
    [_subView addSubview:view];
    return YES;
}


//  Alert
- (void) message:(NSString *)message
{
//	UIAlertView	*aView	= [[UIAlertView alloc]
//						   initWithTitle:@"UPOS Sample"
//						   message:message
//						   delegate:nil
//						   cancelButtonTitle:NSLocalizedString(@"Confirm", @"")
//						   otherButtonTitles:nil];
//	//self.alertView	= aView;
//	[aView show];
//	[aView release];
	
}

-(NSString*) getStringForState:(NSInteger)State
{
    switch (State) {
        case UPOS_S_CLOSED:
            return @"UPOS_S_CLOSED";
        case UPOS_S_IDLE:
            return @"UPOS_S_IDLE";
        case UPOS_S_BUSY:
            return @"UPOS_S_BUSY";
        case UPOS_S_ERROR:
            return @"UPOS_S_ERROR";
        default:
            return [NSString stringWithFormat:@"%ld", (long)State];
    }
}

-(NSString*) getStringForExtendedResultCode:(NSInteger)ExtendedResultCode
{
    switch (ExtendedResultCode) {
            
        case UPOS_E_DEPRECATED:
            return @"UPOS_E_DEPRECATED";

            
        default:
            return [NSString stringWithFormat:@"%ld", (long)ExtendedResultCode];
    }
}
-(NSString*) getStringForResultCode:(NSInteger) ResultCode
{
    
    switch (ResultCode)
    {
        case UPOS_SUCCESS:
            return @"UPOS_SUCCESS";
            
        case UPOS_E_CLOSED:
            return @"UPOS_E_CLOSED";
            
        case UPOS_E_CLAIMED:
            return @"UPOS_E_CLAIMED";
            
        case UPOS_E_NOTCLAIMED:
            return @"UPOS_E_NOTCLAIMED";
            
        case UPOS_E_NOSERVICE:
            return @"UPOS_E_NOSERVICE";
            
        case UPOS_E_DISABLED:
            return @"UPOS_E_DISABLED";
            
        case UPOS_E_ILLEGAL:
            return @"UPOS_E_ILLEGAL";
            
        case UPOS_E_NOHARDWARE:
            return @"UPOS_E_NOHARDWARE";
            
        case UPOS_E_OFFLINE:
            return @"UPOS_E_OFFLINE";
            
        case UPOS_E_NOEXIST:
            return @"UPOS_E_NOEXIST";
            
        case UPOS_E_EXISTS:
            return @"UPOS_E_EXISTS";
            
        case UPOS_E_FAILURE:
            return @"UPOS_E_FAILURE";
            
        case UPOS_E_TIMEOUT:
            return @"UPOS_E_TIMEOUT";
            
        case UPOS_E_BUSY:
            return @"UPOS_E_BUSY";
            
        case UPOS_E_EXTENDED:
            return @"UPOS_E_EXTENDED";
            
        default:
            return [NSString stringWithFormat:@"%ld", (long)ResultCode];
    }
}

-(void) updateStringEventHistory : (NSString*) string
{
    //  Create Formmat
    NSDate      *now = [NSDate date];
    NSCalendar  *calendar = [NSCalendar currentCalendar];
    NSString* eventsHistory = _uiTextViewHistory.text;
    unsigned int unitFlages = NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit | NSHourCalendarUnit | NSMinuteCalendarUnit | NSSecondCalendarUnit;
    NSDateComponents    *componentsNow = [calendar components:unitFlages fromDate:now];
    
    eventsHistory = [eventsHistory stringByAppendingFormat:@"(%ld/%ld/%ld %02ld:%02ld:%02ld) %@ \r\n", (long)[componentsNow year], (long)[componentsNow month], (long)[componentsNow day], (long)[componentsNow hour], (long)[componentsNow minute], (long)[componentsNow second], string];
    
    //   Display
    _uiTextViewHistory.text = eventsHistory;
    
    //  Scroll Move
    NSRange range = NSMakeRange(_uiTextViewHistory.text.length - 1, 1);
    [_uiTextViewHistory scrollRangeToVisible:range];
    
}
-(void) displayResult
{
    // Status Update
    _segOpenClose.selectedSegmentIndex      = (_uposMSRController.State == UPOS_S_CLOSED)?0:1;
    _segEnableDisable.selectedSegmentIndex  = (NSInteger)_uposMSRController.DeviceEnabled;
    _segClaimRelease.selectedSegmentIndex   = _uposMSRController.Claimed;
    
    _uiTextField_ResultCode.text            = [self getStringForResultCode:_uposMSRController.ResultCode];
    _uiTextField_ResultCodeExtended.text    = [self getStringForExtendedResultCode:_uposMSRController.ResultCodeExtended];
    _uiTextField_State.text                 = [self getStringForState:_uposMSRController.State];
    
}


//////////////////////////////////////////////////////////////////////////////////////
#pragma mark UPOS_EVENTS
- (void) DataEvent:(NSNumber *)Status
{
    NSLog(@"!!!!!!!!!!!!  (MSR) Data Event : %ld !!!!!!!!!!!", (long)Status.integerValue);
    
    [self updateStringEventHistory:[NSString stringWithFormat:@"=============  Data Event  ============="]];
    [self updateStringEventHistory:[NSString stringWithFormat:@"track 1: %@", _uposMSRController.Track1Data]];
    [self updateStringEventHistory:[NSString stringWithFormat:@"track 2: %@", _uposMSRController.Track2Data]];
    [self updateStringEventHistory:[NSString stringWithFormat:@"track 3: %@\r\n\r\n\r\n", _uposMSRController.Track3Data]];
}
- (void)OutputCompleteEvent:(NSNumber*)OutputID
{
    NSLog(@"!!!!!!!!!!!!  Output Complete : %ld !!!!!!!!!!!", (long)OutputID.integerValue);
    NSString *message = [NSString stringWithFormat:@"[OutputCompleteEvent] outputID : %ld", (long)OutputID.integerValue];
    [self updateStringEventHistory:message];
}


- (void)ErrorEvent:(NSNumber*) ErrorCode
 ErrorCodeExtended:(NSNumber*) ErrorCodeExtended
        ErrorLocus:(NSNumber*) ErrorLocus
     ErrorResponse:(NSNumber*) ErrorResponse
{
    NSLog(@"!!!!!!!!!!!!  Error Event !!!!!!!!!!!");
    NSString *message = [NSString stringWithFormat:@"[ErrorEvent] ErrorCode:%ld / ErrorCodeExtended:%ld, ErrorLocus:%ld, ErrorResponse:%ld", (long)ErrorCode.integerValue, (long)ErrorCodeExtended.integerValue, (long)ErrorLocus.integerValue, (long)ErrorResponse.integerValue];
    [self updateStringEventHistory:message];
}

-(void)StatusUpdateEvent:(NSNumber*) Status
{
    NSLog(@"!!!!!!!!!!!!  StatusUpdateEvent : %ld !!!!!!!!!!!", (long)Status.integerValue);
    NSString *message;
    switch([Status integerValue])
    {
        case CASH_SUE_DRAWEROPEN:
            [self message:@"Cash Drawer Opened"];
            message = [NSString stringWithFormat:@"[StatusUpdateEvent] Cash Drawer Opened"];
            break;
        case CASH_SUE_DRAWERCLOSED:
            [self message:@"Cash Drawer Closed"];
            message = [NSString stringWithFormat:@"[StatusUpdateEvent] Cash Drawer Closed"];
            break;
            
        case UPOS_SUE_POWER_OFF:
        case UPOS_SUE_POWER_OFF_OFFLINE:
        case UPOS_SUE_POWER_OFFLINE:
            [self message:@"Device off or offLine"];
            message = [NSString stringWithFormat:@"[StatusUpdateEvent] Device off or offLine"];
            break;
            
        case UPOS_SUE_POWER_ONLINE:
            [self message:@"Device OnLine"];
            message = [NSString stringWithFormat:@"[StatusUpdateEvent] Device OnLine"];
            break;
        default:
            message = [NSString stringWithFormat:@"[StatusUpdateEvent] UNKNOWN"];
    }
    
    [self updateStringEventHistory:message];
    
}

#pragma mark -
//////////////////////////////////////////////////////////////////////////////////////
#pragma mark UITableView dataSource / delegate Methods
//////////////////////////////////////////////////////////////////////////////////////
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView
 numberOfRowsInSection:(NSInteger)section
{
    return [[_deviceList getList] count];
}

- (NSString *)tableView:(UITableView *)tableView
titleForHeaderInSection:(NSInteger)section
{
    return @"";
}

- (NSString *)tableView:(UITableView *)tableView
titleForFooterInSection:(NSInteger)section
{
    return @"";
}

- (UITableViewCell *)getCell:(UITableView *)_tableView
{
	static NSString	*reuseId	= @"DeviceCell";
	
    UITableViewCell	*cell	= [_tableView dequeueReusableCellWithIdentifier:reuseId];
	
	if( nil == cell )
	{
        cell    = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault
                                         reuseIdentifier:nil];//reuseId];
        [cell autorelease];
	}
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView
heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    NSInteger height = 35;
	return (height=35);
}


///////////////////////////////////////////////////////////////////////////////////
// 보여줄 Cell 생성
///////////////////////////////////////////////////////////////////////////////////
- (UITableViewCell *)tableView:(UITableView *)_tableView
         cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell       = [self getCell:_tableView];
    
    
    if(_deviceList)
    {
        if(indexPath.row >= [[_deviceList getList] count])
        {
            return cell;
        }
        
        UPOSMSR      *device  = [[_deviceList getList] objectAtIndex:indexPath.row];
        
        cell.textLabel.text  = device.modelName;  //[NSString stringWithFormat:@"%@ (%@)", device.modelName, device.address];
    }
    
	return cell;
}


///////////////////////////////////////////////////////////////////////////////////
// Printer가 선택되었다.
///////////////////////////////////////////////////////////////////////////////////
- (NSIndexPath *)tableView:(UITableView *)tableView
  willSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ willSelectRowAtIndexPath\r\n");
//    NSLog(@"- willSelectRowAtIndexPath\r\n");
	return indexPath;
}

- (NSIndexPath *)tableView:(UITableView *)tableView
willDeselectRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ willDeselectRowAtIndexPath\r\n");
//    NSLog(@"- willDeselectRowAtIndexPath\r\n");
	return indexPath;
}

- (void)tableView:(UITableView *)tableView
didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ didSelectRowAtIndexPath\r\n");
//    Device* device  = [[_deviceList getList]" objectAtIndex:indexPath.row];
//    _labelName.text     = [NSString stringWithFormat:@"%@",device.modelName];
//    _labelLDN.text      = [NSString stringWithFormat:@"%@",device.ldn];
//    switch ([device.interfaceType intValue])
//    {
//        case 1: // Ethernet
//        case 2: // Wifi
//            _labelPort.text     = [NSString stringWithFormat:@"IP_%@:%@",device.address, device.port];
//            
//            break;
//        case 4: // BT
//            _labelPort.text     = [NSString stringWithFormat:@"BT_%@",device.address];
//            break;
//    }
//    //    _labelPort.text     = [NSString stringWithFormat:@"%@",device.port];
//    
//    NSLog(@"- didSelectRowAtIndexPath\r\n");
}

- (void)tableView:(UITableView *)tableView
commitEditingStyle:(UITableViewCellEditingStyle)editingStyle
forRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ commitEditingStyle\r\n");
//    NSLog(@"- commitEditingStyle\r\n");
}

- (BOOL)tableView:(UITableView *)tableView
canEditRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ canEditRowAtIndexPath\r\n");
//    NSLog(@"- canEditRowAtIndexPath\r\n");
	return YES;
}

- (UITableViewCellEditingStyle)tableView:(UITableView *)tableView
           editingStyleForRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ editingStyleForRowAtIndexPath\r\n");
//    NSLog(@"- editingStyleForRowAtIndexPath\r\n");
	return UITableViewCellEditingStyleNone;
}

- (void)tableView:(UITableView *)tableView
willBeginEditingRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ willBeginEditingRowAtIndexPath\r\n");
//    NSLog(@"- willBeginEditingRowAtIndexPath\r\n");
}

- (void)tableView:(UITableView *)tableView
didEndEditingRowAtIndexPath:(NSIndexPath *)indexPath
{
//    NSLog(@"+ didEndEditingRowAtIndexPath\r\n");
//    NSLog(@"- didEndEditingRowAtIndexPath\r\n");
}
// (+)bixolon[2011.08.02] : End  tableView's Delegate


/********************************************************/
//  IBActions..
- (IBAction)changeSubViewValue:(UISegmentedControl *)sender
{
    if([_subViewList count] <= sender.selectedSegmentIndex)
        return;
    [self doChangeSubView:[_subViewList objectAtIndex:sender.selectedSegmentIndex]];
    
}

- (IBAction)printerOpenClose:(UISegmentedControl*)sender
{
    NSIndexPath*    indexPath = [_tblMSRList indexPathForSelectedRow];
    UPOSMSR* device  = [[_deviceList getList] objectAtIndex:indexPath.row];

    if(sender.selectedSegmentIndex == 0)
    {
        _uposResult = [_uposMSRController close];
    }
    else
    {
        _uposResult = [_uposMSRController open:device.modelName];
    }
//    [self displayResult:_uposResult];
    
    [self displayResult];
    
}
- (IBAction)printerClaimRelease:(UISegmentedControl*)sender
{
    if(sender.selectedSegmentIndex == 0)
    {
        _uposResult = [_uposMSRController releaseDevice];
    }
    else
    {
        _uposResult = [_uposMSRController claim:5000];
    }
    //    [self displayResult:_uposResult];
    
    [self displayResult];
}
- (IBAction)printerEnableDisable:(UISegmentedControl*)sender
{
    if(sender.selectedSegmentIndex == 0)
    {
        _uposMSRController.DeviceEnabled = NO;
    }
    else
    {
        _uposMSRController.DeviceEnabled = YES;
    }
    
    [self displayResult];
}


- (IBAction)onGetStatus:(id)sender
{
//    _uposMSRController State
    [self displayResult];
}


- (IBAction)onButton_AddDevice:(id)sender {
    //    _subViewAddMSR popoverPresentationController
    
    //    _subViewAddMSR.modalPresentationStyle = UIModalPresentationPopover;
    //    [self presentViewController:_subViewAddMSR animated:YES completion:nil];
    //
    
    [_subViewAddMSR parent:self];
    _subViewAddMSR.supportedModelList = [_uposMSRController getSupportDeviceStrings];
    
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad) {
        UIView *anchor = sender;
        _popOver = [[UIPopoverController alloc]
                    initWithContentViewController:_subViewAddMSR];
        [_popOver presentPopoverFromRect:anchor.frame
                                  inView:anchor.superview
                permittedArrowDirections:UIPopoverArrowDirectionAny animated:YES];
    }
    else
    {
        [self presentViewController:_subViewAddMSR animated:YES completion:nil];
    }
}

/***********************************************************/
//  Call to Method for Printer for SubViews Menu
-(void) addMSR : (UPOSMSR*)msr
{
    [_deviceList addDevice:msr];
    [_tblMSRList reloadData];
}

@end




















