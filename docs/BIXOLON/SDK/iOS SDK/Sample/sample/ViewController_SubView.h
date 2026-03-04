//
//  ViewController_SubView.h
//  Sample
//
//  Created by savin on 13. 11. 14..
//  Copyright (c) 2013년 savin. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ViewController_Printer.h"

@interface ViewController_SubView : UIViewController
{
    ViewController_Printer*     _parentView;
}

-(void) parent:(ViewController_Printer*)viewController;
@end
