//
//  ViewController_PrinterSubViewEventHistory.m
//  Sample
//
//  Created by savin on 13. 11. 19..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_PrinterSubViewEventHistory.h"

@interface ViewController_PrinterSubViewEventHistory ()

@end

@implementation ViewController_PrinterSubViewEventHistory

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
    _uiTextViewHistory.text = @"";
    _uiTextViewHistory.editable = NO;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (IBAction)clearStringEventHistrory:(id)sender
{
    _uiTextViewHistory.text = @"";
}

-(void) updateStringEventHistory:(NSString*) string
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

- (void)dealloc {
    
    [_uiTextViewHistory release];
    [super dealloc];
}
@end
