
// SamplePg_VC++.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CSamplePg_VCApp:
// See SamplePg_VC++.cpp for the implementation of this class
//

class CSamplePg_VCApp : public CWinAppEx
{
public:
	CSamplePg_VCApp();

// Overrides
	public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CSamplePg_VCApp theApp;