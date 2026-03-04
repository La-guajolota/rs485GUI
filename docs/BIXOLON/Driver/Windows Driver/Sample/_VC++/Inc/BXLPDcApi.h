#define BXLPDC_API __declspec(dllimport)

//	Rotation
#define ROTATE_0	0
#define ROTATE_90	1
#define ROTATE_180	2
#define ROTATE_270	3

BXLPDC_API BOOL	__stdcall ConnectPrinter(LPCSTR szPrinterName);
BXLPDC_API BOOL	__stdcall ConnectPrinterW(LPWSTR szPrinterName);

BXLPDC_API VOID	__stdcall DisconnectPrinter();
BXLPDC_API BOOL	__stdcall Start_Doc(LPCSTR szDocName);
BXLPDC_API BOOL	__stdcall Start_DocW(LPWSTR szDocName);
BXLPDC_API VOID	__stdcall End_Doc();
BXLPDC_API BOOL	__stdcall Start_Page();
BXLPDC_API VOID	__stdcall End_Page();

BXLPDC_API INT __stdcall PrintBitmap(INT nPositionX, INT nPositionY, LPCSTR bitmapFile);
BXLPDC_API INT __stdcall PrintBitmapW(INT nPositionX, INT nPositionY, LPWSTR bitmapFile);

BXLPDC_API INT __stdcall PrintDeviceFont(INT nPositionX, 
										 INT nPositionY, 
										 LPCSTR szFontName, 
										 INT nFontSize, 
										 LPCSTR szData);

BXLPDC_API INT __stdcall PrintDeviceFontW(INT nPositionX, 
										  INT nPositionY, 
										  LPWSTR szFontName, 
										  INT nFontSize, 
										  LPWSTR szData);

BXLPDC_API INT __stdcall PrintTrueFont(INT nPositionX, 
									   INT nPositionY, 
									   LPCSTR szFontName, 
									   INT nFontSize, 
									   LPCSTR szData, 
									   BOOL bBold = FALSE, 
									   int nRotation = ROTATE_0, 
									   BOOL bItalic = FALSE, 
									   BOOL bUnderline = FALSE);

BXLPDC_API INT __stdcall PrintTrueFontW(INT nPositionX, 
										INT nPositionY, 
										LPWSTR szFontName, 
										INT nFontSize, 
										LPWSTR szData, 
										BOOL bBold = FALSE, 
										int nRotation = ROTATE_0, 
										BOOL bItalic = FALSE, 
										BOOL bUnderline = FALSE);
