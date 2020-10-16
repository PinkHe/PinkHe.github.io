    #include <windows.h>
     
    LRESULT CALLBACK MyProc(HWND hwnd,UINT message,WPARAM wParam,LPARAM lParam);
     
    int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd )
    {
         MSG      msg;
         HWND     hwnd;
         static TCHAR szAppName[] = "hl";
     
         WNDCLASS wndclass;
         wndclass.style        = CS_HREDRAW | CS_VREDRAW;
         wndclass.cbClsExtra   = 0;
         wndclass.cbWndExtra   = 0;
         wndclass.lpfnWndProc  = MyProc;
         wndclass.hInstance    = hInstance;
         wndclass.hIcon        = LoadIcon(NULL,IDI_APPLICATION);
         wndclass.hCursor      = LoadCursor(NULL,IDC_ARROW);
         wndclass.hbrBackground= (HBRUSH)GetStockObject(WHITE_BRUSH);
         wndclass.lpszMenuName = NULL;
         wndclass.lpszClassName= szAppName;
     
         if(!RegisterClass(&wndclass))
         {
              MessageBox(NULL,TEXT("error"),TEXT("title"),MB_ICONERROR);
              return 0;
         }
         hwnd = CreateWindow(szAppName,
                                  TEXT("Hello"),
                                  WS_OVERLAPPEDWINDOW,
                                  CW_USEDEFAULT,
                                  CW_USEDEFAULT,
                                  CW_USEDEFAULT,
                                  CW_USEDEFAULT,
                                  NULL,
                                  NULL,
                                  hInstance,
                                  NULL
                                  );
         ShowWindow(hwnd,nShowCmd);
         UpdateWindow(hwnd);
     
         while(GetMessage(&msg,hwnd,0,0))
         {
              TranslateMessage(&msg);
              DispatchMessage(&msg);
         }
         return msg.wParam;
    }
     
    LRESULT CALLBACK MyProc(HWND hwnd,UINT message,WPARAM wParam,LPARAM lParam)
    {
     
         switch(message)
         {
         case WM_DESTROY:
              PostQuitMessage(0);
              return 0;
         }
         return DefWindowProc(hwnd,message,wParam,lParam);
    }