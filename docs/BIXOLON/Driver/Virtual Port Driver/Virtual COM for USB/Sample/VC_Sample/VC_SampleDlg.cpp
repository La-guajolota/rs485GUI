// VC_SampleDlg.cpp : implementation file
//

#include "stdafx.h"
#include "VC_Sample.h"
#include "VC_SampleDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CVC_SampleDlg dialog

CVC_SampleDlg::CVC_SampleDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CVC_SampleDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CVC_SampleDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	m_hMyDevice=NULL;
}

void CVC_SampleDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CVC_SampleDlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CVC_SampleDlg, CDialog)
	//{{AFX_MSG_MAP(CVC_SampleDlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(ID_TEST_PRINT, OnTestPrint)
	ON_WM_CLOSE()
	ON_BN_CLICKED(ID_TEST_LABELPRINT, OnTestLabelprint)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CVC_SampleDlg message handlers

BOOL CVC_SampleDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	// Open using Virtual Com port(COM16)
	m_hMyDevice =  CreateFile("\\\\.\\COM16",
							GENERIC_READ|GENERIC_WRITE,
							0,
							NULL,
							OPEN_EXISTING,
							FILE_ATTRIBUTE_NORMAL,
							NULL);


	// Open Error Handling
	if(m_hMyDevice==INVALID_HANDLE_VALUE||m_hMyDevice==NULL)
	{
		AfxMessageBox("Unable to open the device...");
	}


	// Get Communication State of Virtual COM port
	if(!GetCommState(m_hMyDevice,&m_dcb))
	{
		AfxMessageBox("Get CommState Fail...");
	}

	m_dcb.BaudRate=115200;
	m_dcb.ByteSize=8;
	m_dcb.fDsrSensitivity=TRUE;

	m_dcb.fOutxCtsFlow=FALSE;
	m_dcb.fOutxDsrFlow=TRUE;

	m_dcb.fRtsControl=RTS_CONTROL_DISABLE;
	m_dcb.fDtrControl=DTR_CONTROL_ENABLE;


	// Set Communication State
	if(!SetCommState(m_hMyDevice,&m_dcb))
	{
		AfxMessageBox("Set CommState Fail...");
	}
	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CVC_SampleDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CVC_SampleDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

// for POS Printer
void CVC_SampleDlg::OnTestPrint() 
{
	// TODO: Add your control notification handler code here
	
	DWORD dwWritten = 0;
	
	//Feed and Cutting
	unsigned char command[]="\x1d\x56\x41\x00";
	
	dwWritten=Write((unsigned char*)"===================================\x0d\x0a",38);
	dwWritten=Write((unsigned char*)"====Virtual COM for USB Driver=====\x0d\x0a",38);
	dwWritten=Write((unsigned char*)"\x0d\x0a",2);
	dwWritten=Write((unsigned char*)"======Visual C++ Sample Code=======\x0d\x0a",38);
	dwWritten=Write((unsigned char*)"===================================\x0d\x0a",38);
	dwWritten=Write(command, 4);

}

// for Label Printer
void CVC_SampleDlg::OnTestLabelprint() 
{
	DWORD dwWritten = 0;

	char szText1[] = "T50,100,3,1,1,0,0,N,N,'==================================='\r\n";
	char szText2[] = "T50,150,3,1,1,0,0,N,N,'====Virtual COM for USB Driver====='\r\n";
	char szText3[] = "T50,200,3,1,1,0,0,N,N,'======Visual C++ Sample Code======='\r\n";
	char szText4[] = "T50,250,3,1,1,0,0,N,N,'==================================='\r\n";

	dwWritten=Write((unsigned char*)szText1, strlen(szText1));
	dwWritten=Write((unsigned char*)szText2, strlen(szText2));
	dwWritten=Write((unsigned char*)szText3, strlen(szText3));
	dwWritten=Write((unsigned char*)szText4, strlen(szText4));
	dwWritten=Write((unsigned char*)"P1\r\n", 4); // Prints...
}

// Write File Function
DWORD CVC_SampleDlg::Write(BYTE *pByte, DWORD dwWritten)
{
	DWORD dwWrittenResult=0;
	DWORD dwTotalWritten = 0;

	if(WriteFile(m_hMyDevice, pByte, dwWritten, &dwWrittenResult, NULL)==0)
	{
		AfxMessageBox("Write Failed...");
		return 0;

	}
	
	return dwWrittenResult;
}



void CVC_SampleDlg::OnClose() 
{
	// TODO: Add your message handler code here and/or call default
	
	// Close Hande
	if(m_hMyDevice!=NULL)
	{
		CloseHandle(m_hMyDevice);
	}
	

	CDialog::OnClose();
}


// ReadFile function
DWORD CVC_SampleDlg::Read(BYTE *pByte, DWORD dwRead)
{
	if(ReadFile(m_hMyDevice, (LPVOID)pByte, dwRead, &dwRead, NULL)==0)
	{
		AfxMessageBox("Read Failed...");
		return 0;

	}
	
	return dwRead;
}

