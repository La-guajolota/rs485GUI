// VC_SampleDlg.h : header file
//

#if !defined(AFX_VC_SAMPLEDLG_H__3A09972F_3E23_4A36_88C2_4F925D40328D__INCLUDED_)
#define AFX_VC_SAMPLEDLG_H__3A09972F_3E23_4A36_88C2_4F925D40328D__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CVC_SampleDlg dialog

class CVC_SampleDlg : public CDialog
{
// Construction
public:
	DWORD Read(BYTE *pByte, DWORD dwRead);
	DCB m_dcb;
	HANDLE m_hMyDevice;
	DWORD Write(BYTE *pByte, DWORD dwWritten);
	CVC_SampleDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CVC_SampleDlg)
	enum { IDD = IDD_VC_SAMPLE_DIALOG };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CVC_SampleDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CVC_SampleDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnTestPrint();
	afx_msg void OnClose();
	afx_msg void OnTestLabelprint();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_VC_SAMPLEDLG_H__3A09972F_3E23_4A36_88C2_4F925D40328D__INCLUDED_)
