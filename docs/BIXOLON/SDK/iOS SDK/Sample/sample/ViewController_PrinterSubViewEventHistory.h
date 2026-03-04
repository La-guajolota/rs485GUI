//
//  ViewController_PrinterSubViewEventHistory.h
//  Sample
//
//  Created by savin on 13. 11. 19..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import "ViewController_SubView.h"

@interface ViewController_PrinterSubViewEventHistory : ViewController_SubView
{
    IBOutlet UITextView *_uiTextViewHistory;
}

- (IBAction)clearStringEventHistrory:(id)sender;
-(void) updateStringEventHistory : (NSString*) string;
@end
